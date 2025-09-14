#!/usr/bin/env python3
"""
gpu_demo.py — Minimal CPU vs GPU timing demo from the command line.

- CPU path: NumPy vectorized math on large arrays
- GPU path: CuPy (CUDA) vectorized math on the same arrays
- Prints elapsed time and speedup

Tip: Use a larger --size for clearer GPU win (e.g., 10_000_000). Very small sizes
can be slower on GPU due to data transfer/launch overheads.
"""

import argparse
import time
import sys

# Try to import NumPy (CPU) and CuPy (GPU)
try:
    import numpy as np
except Exception as e:
    print("NumPy is required. Install with: pip install numpy")
    sys.exit(1)

try:
    import cupy as cp  # GPU (CUDA)
    CUPY_AVAILABLE = True
except Exception:
    CUPY_AVAILABLE = False

def human_time(seconds: float) -> str:
    """Nicely format elapsed seconds."""
    if seconds < 1e-3:
        return f"{seconds * 1e6:.2f} µs"
    if seconds < 1:
        return f"{seconds * 1e3:.2f} ms"
    return f"{seconds:.3f} s"

def cpu_run(n: int, repeats: int) -> float:
    """
    Perform a simple numeric workload on CPU:
    - Allocate arrays
    - Do a fused arithmetic expression several times
    - Return the best (min) elapsed time across repeats
    """
    # Create inputs once (so allocation cost doesn't dominate inside the loop)
    a = np.linspace(0, 1, n, dtype=np.float32)
    b = np.linspace(1, 2, n, dtype=np.float32)

    best = float("inf")
    for _ in range(repeats):
        start = time.perf_counter()
        # "Workload": ~5 ops/element (mul/add/sin/sqrt)
        # You can tweak this expression to change arithmetic intensity
        c = np.sin(a * b + 0.1) + np.sqrt(a + 0.5) * 0.25
        # Force computation to finish (NumPy is eager, so this is immediate)
        _ = c.sum()  # cheap reduction to avoid dead-code elimination
        elapsed = time.perf_counter() - start
        best = min(best, elapsed)
    return best

def gpu_run(n: int, repeats: int) -> float:
    """
    Perform the same workload on GPU (CuPy).
    Returns best (min) elapsed time across repeats, including compute but
    excluding initial one-time warmup/alloc cost.
    """
    if not CUPY_AVAILABLE:
        raise RuntimeError("CuPy not available")

    # Allocate on device once
    a = cp.linspace(0, 1, n, dtype=cp.float32)
    b = cp.linspace(1, 2, n, dtype=cp.float32)

    # Warm-up run (JIT + kernels + caches)
    _ = cp.sin(a * b + 0.1) + cp.sqrt(a + 0.5) * 0.25
    cp.cuda.Stream.null.synchronize()

    best = float("inf")
    for _ in range(repeats):
        start = time.perf_counter()
        c = cp.sin(a * b + 0.1) + cp.sqrt(a + 0.5) * 0.25
        # Ensure GPU finished before timing stops
        _ = cp.sum(c)
        cp.cuda.Stream.null.synchronize()
        elapsed = time.perf_counter() - start
        best = min(best, elapsed)
    return best

def main():
    parser = argparse.ArgumentParser(
        description="CPU vs GPU timing demo (NumPy vs CuPy)."
    )
    parser.add_argument(
        "--size", type=int, default=1_000_000,
        help="Number of elements (operations scale with size). Example: 1000 or 10_000_000."
    )
    parser.add_argument(
        "--repeats", type=int, default=5,
        help="Number of timing repeats; best time is reported."
    )
    parser.add_argument(
        "--cpu-only", action="store_true",
        help="Run CPU path only (useful for machines without GPU)."
    )
    parser.add_argument(
        "--gpu-only", action="store_true",
        help="Run GPU path only. Fails if CuPy/CUDA not installed."
    )
    args = parser.parse_args()

    n = args.size
    repeats = args.repeats

    print("="*70)
    print(f"Vector size: {n:,}")
    print(f"Repeats: {repeats}")
    print(f"CuPy available: {CUPY_AVAILABLE}")
    print("="*70)

    cpu_time = None
    gpu_time = None

    if not args.gpu_only:
        print("Running CPU (NumPy)...")
        cpu_time = cpu_run(n, repeats)
        print(f"CPU best time: {human_time(cpu_time)}")

    if not args.cpu_only:
        if not CUPY_AVAILABLE:
            print("\nGPU run skipped — CuPy not found.")
            print("To enable GPU: install NVIDIA drivers + CUDA Toolkit and then:")
            print("  pip install cupy-cuda12x   # pick the wheel matching your CUDA")
            print("See: https://docs.cupy.dev/en/stable/install.html")
        else:
            print("\nRunning GPU (CuPy/CUDA)...")
            try:
                # Show basic device info
                dev = cp.cuda.Device()
                print(f"GPU device: {cp.cuda.runtime.getDeviceProperties(dev.id)['name'].decode()}")
            except Exception:
                pass
            gpu_time = gpu_run(n, repeats)
            print(f"GPU best time: {human_time(gpu_time)}")

    # Summary
    print("\n" + "-"*70)
    if cpu_time is not None and gpu_time is not None:
        speedup = cpu_time / gpu_time if gpu_time > 0 else float("inf")
        print(f"Speedup (CPU time / GPU time): {speedup:.2f}×")
    elif cpu_time is not None:
        print("Only CPU ran. Enable GPU to compare.")
    elif gpu_time is not None:
        print("Only GPU ran.")
    else:
        print("Nothing ran. Check your options.")
    print("-"*70)

if __name__ == "__main__":
    main()
