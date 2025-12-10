"""
PYTHON DATA STRUCTURES DEMO
---------------------------
This script demonstrates CRUD + Search operations for:
- List
- Tuple
- Set
- Dictionary
- Stack (using list)
- Queue (using collections.deque)
- Singly Linked List (custom Node class)

Each section includes:
- Educational notes (properties, use-cases)
- Clean functions per operation with verbose logs
- ASCII visualizations after major steps
- A main() runner to execute demos in sequence
"""

from collections import deque
from typing import Any, Optional


# ============================================================
# ============ PRINTING HELPERS & BANNERS ====================
# ============================================================

def banner(title: str) -> None:
    """Print a centered banner with a title."""
    print("\n" + "=" * 56)
    print(f"{title:^56}")
    print("=" * 56)


def sub_header(title: str) -> None:
    """Print a sub-header for sections."""
    print("\n" + "-" * 56)
    print(f"{title}")
    print("-" * 56)


# ============================================================
# ========================= LIST =============================
# ============================================================
# What is a List?
# - Ordered, Mutable, Allows duplicates.
# Core Properties:
# - Indexable sequence, resizing, supports slice operations.
# Common Use Cases:
# - General-purpose collections, dynamic arrays, ordered data.

def visualize_list(items: list[Any]) -> None:
    """ASCII diagram for a list."""
    diagram = " -> ".join(str(x) for x in items) if items else "(empty)"
    print(f"[List] View: {diagram}")

def list_create(initial_items: list[Any]) -> list[Any]:
    """Create a new list with initial items."""
    print("[List] Creating list with items:", initial_items)
    fruit_list = list(initial_items)
    visualize_list(fruit_list)
    return fruit_list

def list_read(fruit_list: list[Any]) -> None:
    """Read and print all elements of the list."""
    print("[List] Reading all elements (index:value):")
    for idx, val in enumerate(fruit_list):
        print(f"  - {idx}: {val}")
    visualize_list(fruit_list)

def list_update_add(fruit_list: list[Any], item: Any) -> None:
    """Append an item to the list."""
    print(f"[List] Adding item: {item}")
    fruit_list.append(item)
    visualize_list(fruit_list)

def list_update_set(fruit_list: list[Any], index: int, new_value: Any) -> None:
    """Update the item at the given index."""
    if 0 <= index < len(fruit_list):
        print(f"[List] Updating index {index} from {fruit_list[index]} to {new_value}")
        fruit_list[index] = new_value
    else:
        print(f"[List] Update skipped: index {index} out of range")
    visualize_list(fruit_list)

def list_delete(fruit_list: list[Any], item: Any) -> None:
    """Delete the first occurrence of an item if present."""
    print(f"[List] Deleting item: {item}")
    try:
        fruit_list.remove(item)
        print(f"[List] Item '{item}' removed.")
    except ValueError:
        print(f"[List] Item '{item}' not found. Nothing removed.")
    visualize_list(fruit_list)

def list_search(fruit_list: list[Any], target: Any) -> int:
    """Search for an item and return its index, or -1 if not found."""
    print(f"[List] Searching for: {target}")
    try:
        idx = fruit_list.index(target)
        print(f"[List] Found at index: {idx}")
        return idx
    except ValueError:
        print("[List] Not found.")
        return -1


# ============================================================
# ======================== TUPLE =============================
# ============================================================
# What is a Tuple?
# - Ordered, Immutable, Allows duplicates.
# Core Properties:
# - Fixed after creation; any "update" creates a new tuple.
# Common Use Cases:
# - Fixed records, dictionary keys (when values are hashable), safe returns.

def visualize_tuple(items: tuple[Any, ...]) -> None:
    """ASCII diagram for a tuple."""
    if items:
        body = " — ".join(str(x) for x in items)
        print(f"[Tuple] View: ( {body} )")
    else:
        print("[Tuple] View: ( empty )")

def tuple_create(initial_items: tuple[Any, ...]) -> tuple[Any, ...]:
    """Create a tuple with initial items."""
    print("[Tuple] Creating tuple with items:", initial_items)
    t = tuple(initial_items)
    visualize_tuple(t)
    return t

def tuple_read(t: tuple[Any, ...]) -> None:
    """Read and print all elements of the tuple."""
    print("[Tuple] Reading all elements (index:value):")
    for idx, val in enumerate(t):
        print(f"  - {idx}: {val}")
    visualize_tuple(t)

def tuple_update_add(t: tuple[Any, ...], item: Any) -> tuple[Any, ...]:
    """'Update' by creating a new tuple with an appended item."""
    print(f"[Tuple] Tuples are immutable. Creating new tuple with added item: {item}")
    new_tuple = t + (item,)
    visualize_tuple(new_tuple)
    return new_tuple

def tuple_delete(t: tuple[Any, ...], item: Any) -> tuple[Any, ...]:
    """'Delete' by creating a new tuple without the first matching item."""
    print(f"[Tuple] Tuples are immutable. Creating new tuple without item: {item}")
    if item in t:
        idx = t.index(item)
        new_tuple = t[:idx] + t[idx+1:]
    else:
        print("[Tuple] Item not found. Returning original tuple.")
        new_tuple = t
    visualize_tuple(new_tuple)
    return new_tuple

def tuple_search(t: tuple[Any, ...], target: Any) -> int:
    """Search for an item, return index or -1."""
    print(f"[Tuple] Searching for: {target}")
    try:
        idx = t.index(target)
        print(f"[Tuple] Found at index: {idx}")
        return idx
    except ValueError:
        print("[Tuple] Not found.")
        return -1


# ============================================================
# ========================== SET =============================
# ============================================================
# What is a Set?
# - Unordered, Mutable, No duplicates.
# Core Properties:
# - Fast membership tests, no indexing, elements must be hashable.
# Common Use Cases:
# - Membership checks, removing duplicates, set algebra.

def visualize_set(items: set[Any]) -> None:
    """ASCII diagram for a set."""
    if items:
        body = " , ".join(str(x) for x in sorted(items, key=str))
        print(f"[Set] View: {{ {body} }}")
    else:
        print("[Set] View: { } (empty)")

def set_create(initial_items: set[Any]) -> set[Any]:
    """Create a set with initial items."""
    print("[Set] Creating set with items:", initial_items)
    s = set(initial_items)
    visualize_set(s)
    return s

def set_read(color_set: set[Any]) -> None:
    """Read and print all elements of the set."""
    print("[Set] Reading all elements (unordered):")
    for val in sorted(color_set, key=str):
        print(f"  - {val}")
    visualize_set(color_set)

def set_update_add(color_set: set[Any], item: Any) -> None:
    """Add an item to the set (no effect if duplicate)."""
    print(f"[Set] Adding item: {item}")
    pre_size = len(color_set)
    color_set.add(item)
    post_size = len(color_set)
    if post_size == pre_size:
        print("[Set] Item already existed; no change.")
    visualize_set(color_set)

def set_delete(color_set: set[Any], item: Any) -> None:
    """Remove an item if present."""
    print(f"[Set] Deleting item: {item}")
    if item in color_set:
        color_set.remove(item)
        print("[Set] Item removed.")
    else:
        print("[Set] Item not found; nothing removed.")
    visualize_set(color_set)

def set_search(color_set: set[Any], target: Any) -> bool:
    """Check membership of an item."""
    print(f"[Set] Searching for: {target}")
    found = target in color_set
    print(f"[Set] Found: {found}")
    return found


# ============================================================
# ====================== DICTIONARY ==========================
# ============================================================
# What is a Dictionary?
# - Unordered (insertion-ordered since Python 3.7+), Mutable, Unique keys.
# Core Properties:
# - Key -> Value mapping, fast lookups by key.
# Common Use Cases:
# - Records, configurations, fast associative lookups.

def visualize_dict(mapping: dict[Any, Any]) -> None:
    """ASCII diagram for a dictionary."""
    if not mapping:
        print("[Dict] View: <empty>")
        return
    print("[Dict] View (key → value):")
    for k in mapping:
        print(f"  [{k}] → ({mapping[k]})")

def dict_create(initial_mapping: dict[Any, Any]) -> dict[Any, Any]:
    """Create a dictionary with initial key-value pairs."""
    print("[Dict] Creating dictionary with items:", initial_mapping)
    student_records = dict(initial_mapping)
    visualize_dict(student_records)
    return student_records

def dict_read(student_records: dict[Any, Any]) -> None:
    """Read and print all key-value pairs."""
    print("[Dict] Reading all key-value pairs:")
    for key, value in student_records.items():
        print(f"  - {key}: {value}")
    visualize_dict(student_records)

def dict_update_add(student_records: dict[Any, Any], key: Any, value: Any) -> None:
    """Add or update a key with a value."""
    action = "Updating" if key in student_records else "Adding"
    print(f"[Dict] {action} key '{key}' with value '{value}'")
    student_records[key] = value
    visualize_dict(student_records)

def dict_delete(student_records: dict[Any, Any], key: Any) -> None:
    """Delete a key if present."""
    print(f"[Dict] Deleting key: {key}")
    if key in student_records:
        del student_records[key]
        print("[Dict] Key removed.")
    else:
        print("[Dict] Key not found; nothing removed.")
    visualize_dict(student_records)

def dict_search(student_records: dict[Any, Any], key: Any) -> Optional[Any]:
    """Search for a value by key; return value or None if not found."""
    print(f"[Dict] Searching for key: {key}")
    if key in student_records:
        print(f"[Dict] Found. Value: {student_records[key]}")
        return student_records[key]
    print("[Dict] Not found.")
    return None


# ============================================================
# ====================== STACK (LIST) ========================
# ============================================================
# What is a Stack?
# - LIFO (Last-In, First-Out), use list with append()/pop().
# Core Properties:
# - Push/Pop on one end (top).
# Common Use Cases:
# - Undo history, call stacks, balanced symbols.

def visualize_stack(stack: list[Any]) -> None:
    """ASCII diagram for a stack (top at the right)."""
    print("[Stack] View (top ↓):")
    if not stack:
        print("  | empty |")
        return
    for item in reversed(stack):
        print(f"  +-------+\n  | {item:^5} |")
    print("  +-------+")

def stack_push(stack: list[Any], item: Any) -> None:
    """Push an item onto the stack."""
    print(f"[Stack] Push: {item}")
    stack.append(item)
    visualize_stack(stack)

def stack_pop(stack: list[Any]) -> Optional[Any]:
    """Pop the top item from the stack."""
    print("[Stack] Pop operation")
    if stack:
        item = stack.pop()
        print(f"[Stack] Popped: {item}")
    else:
        item = None
        print("[Stack] Stack is empty; nothing popped.")
    visualize_stack(stack)
    return item

def stack_peek(stack: list[Any]) -> Optional[Any]:
    """Peek at the top item without removing it."""
    print("[Stack] Peek operation")
    top = stack[-1] if stack else None
    print(f"[Stack] Top: {top}")
    visualize_stack(stack)
    return top

def stack_search(stack: list[Any], target: Any) -> int:
    """Search for an item from top to bottom; return depth (0=top) or -1."""
    print(f"[Stack] Searching for: {target}")
    for depth, item in enumerate(reversed(stack)):
        if item == target:
            print(f"[Stack] Found at depth {depth} from top")
            return depth
    print("[Stack] Not found.")
    return -1


# ============================================================
# ===================== QUEUE (DEQUE) ========================
# ============================================================
# What is a Queue?
# - FIFO (First-In, First-Out).
# Core Properties:
# - Enqueue at rear, dequeue at front.
# Common Use Cases:
# - Task scheduling, buffering, breadth-first traversal.

def visualize_queue(q: deque[Any]) -> None:
    """ASCII diagram for a queue (front to rear)."""
    if not q:
        print("[Queue] View: front | (empty) | rear")
        return
    body = " <- ".join(str(x) for x in q)
    print(f"[Queue] View: front | {body} | rear")

def queue_enqueue(q: deque[Any], item: Any) -> None:
    """Add an item at the rear."""
    print(f"[Queue] Enqueue: {item}")
    q.append(item)
    visualize_queue(q)

def queue_dequeue(q: deque[Any]) -> Optional[Any]:
    """Remove an item from the front."""
    print("[Queue] Dequeue operation")
    if q:
        item = q.popleft()
        print(f"[Queue] Dequeued: {item}")
    else:
        item = None
        print("[Queue] Queue is empty; nothing dequeued.")
    visualize_queue(q)
    return item

def queue_peek(q: deque[Any]) -> Optional[Any]:
    """Peek at the front item without removing it."""
    print("[Queue] Peek operation")
    front = q[0] if q else None
    print(f"[Queue] Front: {front}")
    visualize_queue(q)
    return front

def queue_search(q: deque[Any], target: Any) -> int:
    """Search for an item; return 0-based index from front or -1."""
    print(f"[Queue] Searching for: {target}")
    try:
        idx = list(q).index(target)
        print(f"[Queue] Found at position {idx} from front")
        return idx
    except ValueError:
        print("[Queue] Not found.")
        return -1


# ============================================================
# ================ SINGLY LINKED LIST (CUSTOM) ===============
# ============================================================
# What is a Singly Linked List?
# - A sequence of Nodes; each Node holds data and a pointer to next node.
# Core Properties:
# - Not indexable; operations are O(n) traversal.
# Common Use Cases:
# - Frequent middle insertions/deletions without shifting, low-level structures.

class Node:
    """A Node in a singly linked list."""
    def __init__(self, data: Any):
        self.data: Any = data
        self.next: Optional["Node"] = None

    def __repr__(self) -> str:
        return f"Node({self.data})"

class LinkedList:
    """Singly Linked List with basic CRUD + Search operations and visualization."""
    def __init__(self):
        self.head: Optional[Node] = None

    def visualize(self) -> None:
        """ASCII diagram of the linked list."""
        print("[LinkedList] View:")
        if not self.head:
            print("  None")
            return
        ptr = self.head
        parts = []
        while ptr:
            parts.append(f"[{ptr.data}]")
            ptr = ptr.next
        print("  " + " → ".join(parts) + " → None")

    def insert_end(self, data: Any) -> None:
        """Insert a new node at the end of the list."""
        print(f"[LinkedList] Insert at end: {data}")
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.visualize()
            return
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = new_node
        self.visualize()

    def read_all(self) -> list[Any]:
        """Traverse and return all data values."""
        print("[LinkedList] Reading all nodes:")
        values = []
        ptr = self.head
        idx = 0
        while ptr:
            print(f"  - index {idx}: {ptr.data}")
            values.append(ptr.data)
            ptr = ptr.next
            idx += 1
        self.visualize()
        return values

    def update_first(self, old_value: Any, new_value: Any) -> bool:
        """Update the first node with old_value to new_value."""
        print(f"[LinkedList] Update first '{old_value}' to '{new_value}'")
        ptr = self.head
        while ptr:
            if ptr.data == old_value:
                ptr.data = new_value
                print("[LinkedList] Node updated.")
                self.visualize()
                return True
            ptr = ptr.next
        print("[LinkedList] Value not found; nothing updated.")
        self.visualize()
        return False

    def delete_first(self, target: Any) -> bool:
        """Delete the first node whose data equals target."""
        print(f"[LinkedList] Delete first occurrence of: {target}")
        prev = None
        ptr = self.head
        while ptr:
            if ptr.data == target:
                if prev:
                    prev.next = ptr.next
                else:
                    self.head = ptr.next
                print("[LinkedList] Node deleted.")
                self.visualize()
                return True
            prev = ptr
            ptr = ptr.next
        print("[LinkedList] Value not found; nothing deleted.")
        self.visualize()
        return False

    def search(self, target: Any) -> int:
        """Return index of target or -1 if not found."""
        print(f"[LinkedList] Searching for: {target}")
        idx = 0
        ptr = self.head
        while ptr:
            if ptr.data == target:
                print(f"[LinkedList] Found at index: {idx}")
                self.visualize()
                return idx
            ptr = ptr.next
            idx += 1
        print("[LinkedList] Not found.")
        self.visualize()
        return -1


# ============================================================
# ====================== DEMONSTRATIONS ======================
# ============================================================

def demo_list() -> None:
    sub_header("LIST DEMO")
    fruits = list_create(["apple", "banana", "cherry"])
    list_read(fruits)
    list_update_add(fruits, "dragonfruit")
    list_update_set(fruits, 1, "blueberry")
    list_delete(fruits, "apple")
    list_search(fruits, "cherry")

def demo_tuple() -> None:
    sub_header("TUPLE DEMO")
    coords = tuple_create((10, 20, 30))
    tuple_read(coords)
    coords = tuple_update_add(coords, 40)
    coords = tuple_delete(coords, 20)
    tuple_search(coords, 30)

def demo_set() -> None:
    sub_header("SET DEMO")
    colors = set_create({"red", "green", "blue"})
    set_read(colors)
    set_update_add(colors, "green")  # duplicate test
    set_update_add(colors, "yellow")
    set_delete(colors, "red")
    set_search(colors, "blue")

def demo_dict() -> None:
    sub_header("DICTIONARY DEMO")
    students = dict_create({"Alice": 85, "Bob": 78})
    dict_read(students)
    dict_update_add(students, "Charlie", 92)
    dict_update_add(students, "Alice", 88)  # update
    dict_delete(students, "Bob")
    dict_search(students, "Charlie")

def demo_stack() -> None:
    sub_header("STACK (LIST) DEMO")
    actions: list[str] = []
    stack_push(actions, "open")
    stack_push(actions, "edit")
    stack_push(actions, "save")
    stack_peek(actions)
    stack_search(actions, "edit")
    stack_pop(actions)
    stack_pop(actions)
    stack_pop(actions)
    stack_pop(actions)  # empty pop

def demo_queue() -> None:
    sub_header("QUEUE (DEQUE) DEMO")
    tasks: deque[str] = deque()
    queue_enqueue(tasks, "task-1")
    queue_enqueue(tasks, "task-2")
    queue_enqueue(tasks, "task-3")
    queue_peek(tasks)
    queue_search(tasks, "task-2")
    queue_dequeue(tasks)
    queue_dequeue(tasks)
    queue_dequeue(tasks)
    queue_dequeue(tasks)  # empty dequeue

def demo_linked_list() -> None:
    sub_header("LINKED LIST DEMO")
    ll = LinkedList()
    ll.insert_end("A")
    ll.insert_end("B")
    ll.insert_end("C")
    ll.read_all()
    ll.update_first("B", "B*")
    ll.delete_first("A")
    ll.search("C")


# ============================================================
# ============================ MAIN ==========================
# ============================================================

def main() -> None:
    banner("======== PYTHON DATA STRUCTURES DEMO ========")
    demo_list()
    demo_tuple()
    demo_set()
    demo_dict()
    demo_stack()
    demo_queue()
    demo_linked_list()
    banner("======== END OF DEMO ========")

if __name__ == "__main__":
    main()


# ============================================================
# ==================== SUMMARY (NOTES) =======================
# ============================================================
"""
SUMMARY TABLE (Conceptual)

+---------------+-------------+----------+------------+-------------------------------+
| Data Structure| Ordered?    | Mutable? | Duplicates | Typical Uses                  |
+---------------+-------------+----------+------------+-------------------------------+
| List          | Yes         | Yes      | Yes        | Dynamic arrays, general lists |
| Tuple         | Yes         | No       | Yes        | Fixed records, safe returns   |
| Set           | No          | Yes      | No         | Membership tests, dedup, math |
| Dictionary    | Insertion   | Yes      | Keys unique| Fast lookups by key           |
| Stack (list)  | LIFO order  | Yes      | Yes        | Undo, recursion, parsing      |
| Queue (deque) | FIFO order  | Yes      | Yes        | Scheduling, buffering, BFS    |
| Linked List   | By links    | Yes      | Yes        | Mid insert/delete, learning   |
+---------------+-------------+----------+------------+-------------------------------+

Notes:
- Lists and tuples are indexable sequences; tuples are immutable.
- Sets eliminate duplicates and enable fast membership checks.
- Dictionaries map keys to values with near O(1) average lookups.
- Stacks (LIFO) and Queues (FIFO) specialize list-like behavior for algorithms.
- Linked lists are node-based; great for insert/delete near pointers, but O(n) search.
"""
