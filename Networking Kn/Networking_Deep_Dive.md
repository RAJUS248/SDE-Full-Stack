# Networking Deep Dive — HTTP, TCP/IP, UDP, WebSockets & APIs (Interview-ready Notes + Hands-on Labs)

> Student-friendly, clear, and practical. Use this as a reference for system design rounds, web/backend interviews, and real-world debugging.

---

## 1) Big Picture: From URL → Pixels on your screen

1. **DNS lookup**: Resolve `app.example.com` → `203.0.113.10`.  
2. **Transport setup**: Open a **TCP** connection (3-way handshake) to port **443** (HTTPS) or **80** (HTTP). If the browser & server agree, they may use **HTTP/2** over TCP or **HTTP/3 (QUIC)** over UDP.  
3. **TLS handshake** (for HTTPS): Negotiate ciphers, exchange keys. After this, requests/responses are encrypted.  
4. **HTTP request**: Method, path, headers, optional body.  
5. **Server work**: App logic, DB/cache calls, compose response.  
6. **HTTP response**: Status code, headers (cache, cookies, compression), body (HTML/JSON/media).  
7. **Render**: Browser parses HTML → fetches CSS/JS/images → more HTTP requests (often in parallel/multiplexed).

---

## 2) What’s inside an HTTP request/response?

### Example (browser → server)
```
GET /feed?cursor=abc HTTP/1.1
Host: www.example.com
User-Agent: Chrome/Edge
Accept: text/html,application/json
Accept-Encoding: br,gzip
Cookie: sessionId=xyz
If-None-Match: "rev-42"
```

### Example (server → browser)
```
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Cache-Control: max-age=3600, public
ETag: "rev-42"
Content-Encoding: br
Set-Cookie: sessionId=xyz; HttpOnly; Secure; SameSite=Lax
```

- **Headers** carry metadata:
  - **Caching**: `Cache-Control`, `ETag`, `Last-Modified`, `Expires`.
  - **Cookies**: Set by server (`Set-Cookie`) and sent by browser (`Cookie`).
  - **Compression**: `Content-Encoding: gzip`/`br` (Brotli).

---

## 3) Deep dive: TCP/IP and how HTTP becomes packets

- **TCP** gives *reliable, ordered, byte-stream delivery*. It uses a **3-way handshake**: `SYN` → `SYN+ACK` → `ACK`, then data flows. Lost packets are **retransmitted**; the receiver **ACKs** what it got.
- **Ports**: Logical endpoints on a host (server port 443 for HTTPS; client picks an **ephemeral port**). The OS demultiplexes packets to the correct socket using the 5-tuple (src IP/port, dst IP/port, protocol).
- **How multiple tabs don’t “mix” data**: Each TCP connection has its own sequence numbers and socket; the kernel hands bytes to the right connection.
- **Routing**: Packets hop across routers (TTL decreases) until the destination; if a packet is lost, TCP retransmits.
- **Security**: With **HTTPS**, payloads are encrypted; even if some other machine sees the packet, it cannot read or modify contents without keys.

---

## 4) UDP: Speed over guarantees

- **UDP** is *connectionless* and *unreliable* (no handshake, no retransmission, no ordering). You send datagrams; some may drop.  
- Perfect for **real-time** apps (VoIP/video/gaming) that prefer timeliness over resends. Lost frames are concealed rather than retransmitted.

---

## 5) WebSockets: Real-time over a single long-lived connection

- **WebSocket** upgrades an HTTP connection (`Upgrade: websocket`) to a full-duplex channel over **TCP**. Ideal for chats, live dashboards, collaborative apps.  
- Keep-alive uses ping/pong frames; messages can be text or binary.

---

## 6) Practical, product-level examples (what real apps use)

- **Regular websites & mobile apps**: **HTTPS (HTTP/2 or HTTP/3)** for requests (REST/GraphQL).  
- **YouTube**: Streams via **MPEG-DASH** over HTTP; many clients use **HTTP/3 (QUIC)** where available.  
- **WhatsApp**:  
  - **Messages**: End-to-end encrypted over TLS-protected channels.  
  - **Voice/Video calls**: Real-time media using **WebRTC building blocks**: ICE + DTLS + **SRTP** over **UDP**.  
- **Instagram**:  
  - **Feeds** fetched over **HTTPS GraphQL APIs**; media via CDN. Uploads use HTTPS.

---

## 7) TCP vs UDP vs WebSockets — when to use what

| Dimension | **TCP (HTTP/1.1/2)** | **UDP (Raw/QUIC/RTP)** | **WebSockets (over TCP)** |
|---|---|---|---|
| Delivery guarantees | Reliable, ordered | Unreliable, unordered | Reliable, ordered |
| Latency | Higher (retransmits) | Lowest (no retransmits) | Low (persistent TCP) |
| Best for | Web/API requests, downloads | Live audio/video, gaming | Chats, live dashboards |
| Encryption | TLS | DTLS/TLS/SRTP/QUIC-TLS | TLS (wss://) |
| Example apps | Web pages, REST APIs | WhatsApp calls, YouTube video | WhatsApp Web, stock tickers |

---

## 8) Interview-grade concepts

- **Idempotent vs Safe**: Safe = GET/HEAD (no state change). Idempotent = PUT/DELETE (same result if repeated).  
- **HTTP/2 HoL blocking**: Streams multiplexed but share TCP; packet loss stalls all. HTTP/3 fixes this with QUIC streams.  
- **ETag vs Last-Modified**: ETag (hash/version); Last-Modified (timestamp).  
- **Cookies security**: Use `HttpOnly`, `Secure`, `SameSite`.  
- **Why UDP for media**: Better to drop than delay; conceal with jitter buffers/FEC.

---

## 9) Minimal, working code

### A) HTTP request (Python)
```python
import requests
r = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print("Status:", r.status_code)
print("Headers:", r.headers)
print("Body:", r.text[:120], "...")
```

### B) HTTP request (Java)
```java
import java.net.http.*;
import java.net.URI;

public class HttpGetDemo {
  public static void main(String[] args) throws Exception {
    HttpClient client = HttpClient.newBuilder().build();
    HttpRequest req = HttpRequest.newBuilder(
      URI.create("https://jsonplaceholder.typicode.com/posts/1")).build();
    HttpResponse<String> resp = client.send(req, HttpResponse.BodyHandlers.ofString());
    System.out.println("Status: " + resp.statusCode());
    System.out.println("Headers: " + resp.headers());
    System.out.println("Body: " + resp.body().substring(0, 120));
  }
}
```

### C) UDP demo (Python)

**Server**
```python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 9999))
print("UDP server on :9999")
while True:
    data, addr = s.recvfrom(2048)
    print("from", addr, ":", data.decode())
    s.sendto(b"ack:"+data, addr)
```

**Client**
```python
import socket
c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
c.sendto(b"hello", ("127.0.0.1", 9999))
print(c.recvfrom(2048))
```

---

## 10) ASCII diagram — TCP handshake → request → response

```
Client                                     Server
  | -- SYN ---------------------------------> |
  | <--------------- SYN + ACK -------------- |
  | -- ACK ---------------------------------> |   TCP connection established
  | -- TLS ClientHello ---------------------> |
  | <-------------- TLS ServerHello --------- |
  | -- HTTP Request ------------------------> |
  | <----- HTTP Response --------------------|
  | -- FIN ---------------------------------> |
  | <------------------------ FIN + ACK ----- |
```

---

## 11) Hands-on Labs

### Lab 1 — Inspect HTTP request (Chrome/Edge DevTools)
1. Open **DevTools (F12)** → **Network**.  
2. Reload page. Click the top request.  
3. Check headers (Request URL, Method, Status, Remote Address).  
4. Check **Timing** (DNS, SSL, TTFB).  
5. Enable cache → see 304 or cached results.

### Lab 2 — Validate caching (ETag/Last-Modified)
1. Pick a CSS/JS asset. Note `ETag` and `Last-Modified`.  
2. Reload with cache disabled → full 200.  
3. Reload normally → 304 Not Modified.

### Lab 3 — Test with **Postman**
1. Make GET to `https://jsonplaceholder.typicode.com/posts/1`.  
2. Inspect headers and body.  
3. Add `If-None-Match` header with last ETag → expect 304.

### Lab 4 — Capture with **Fiddler**
1. Run Fiddler, enable HTTPS decryption.  
2. Open a website; inspect sessions.  
3. Replay a request; modify headers; observe differences.

---

## 12) Summary

- **TCP** = reliable; **UDP** = fast but lossy; **WebSockets** = real-time duplex over TCP.  
- **HTTP** rides on these; caching, cookies, compression optimize delivery.  
- Apps mix protocols: REST/GraphQL over HTTPS, UDP for calls, WebSockets for instant updates.  
- Hands-on labs give you visibility into how requests/packets move from browser → server → back.

