
# 📘 Lesson 3 – Transport & Application Protocols

## 📑 Index

1. [TCP vs UDP vs QUIC](#tcp-vs-udp-vs-quic)
2. [HTTP Evolution (0.9 → 3)](#http-evolution-09--3)
3. [Caching, Headers, and Status Codes](#caching-headers-and-status-codes)
4. [Ports & Sockets](#ports--sockets)
5. [APIs vs WebSockets](#apis-vs-websockets)
6. [Summary](#summary)

---

## TCP vs UDP vs QUIC

### 🔹 TCP (Transmission Control Protocol)

* **Reliable, connection-oriented** protocol.
* Features: 3-way handshake, sequencing, retransmission, congestion control.
* Used for: web browsing (HTTP/HTTPS), email (SMTP, IMAP), file transfer (FTP).

📌 **Analogy**: Like a **phone call** — both sides confirm they can hear each other, and corrections happen if words are missed.

---

### 🔹 UDP (User Datagram Protocol)

* **Unreliable, connectionless** protocol.
* No guarantees of delivery, ordering, or retransmission.
* Very fast, used in real-time apps: VoIP, video calls, gaming, live streaming.

📌 **Analogy**: Like **shouting across a room** — no guarantee the listener hears everything, but it’s fast.

---

### 🔹 QUIC (Quick UDP Internet Connections)

* Built on **UDP**, designed by Google.
* Adds reliability, multiplexing, and encryption similar to TCP+TLS but faster.
* Used in **HTTP/3**, improves mobile performance (fewer reconnections).

📌 **Analogy**: Like **express courier delivery** — as fast as UDP but with tracking and security like TCP.

---

## HTTP Evolution (0.9 → 3)

| Version  | Year  | Key Features                                             | Problems Fixed                       |
| -------- | ----- | -------------------------------------------------------- | ------------------------------------ |
| HTTP/0.9 | 1991  | Simple GET only                                          | Too limited                          |
| HTTP/1.0 | 1996  | Headers, more methods                                    | Each request = new connection (slow) |
| HTTP/1.1 | 1997  | Persistent connections, chunked transfer, caching        | Head-of-line blocking                |
| HTTP/2   | 2015  | Multiplexing, binary format, header compression          | Still relies on TCP (HOL blocking)   |
| HTTP/3   | 2020+ | Runs over QUIC, faster handshakes, better mobile support | Complex deployment                   |

📌 **Analogy**:

* HTTP/1.0 → every passenger needs a new taxi.
* HTTP/1.1 → same taxi, multiple trips.
* HTTP/2 → shared bus carrying multiple passengers at once.
* HTTP/3 → high-speed train with encrypted carriages.

---

## Caching, Headers, and Status Codes

### Headers

* **Request headers** → client info, cookies, caching preferences.
* **Response headers** → server details, caching rules, content type.

### Caching

* Saves copies of responses → faster repeat visits.
* Controlled with headers: `Cache-Control`, `ETag`, `Last-Modified`.

📌 **Analogy**: Like keeping a **copy of your favorite book at home** instead of going to the library each time.

### Status Codes

* `200 OK` → success.
* `301/302` → redirection.
* `400` → client error.
* `500` → server error.

📌 **Analogy**: Status codes are like **restaurant order updates**:

* 200 = "Here’s your meal."
* 404 = "Dish not found."
* 500 = "Kitchen problem."

---

## Ports & Sockets

* **Port numbers** identify specific applications on a host.
* Example:

  * HTTP → port 80
  * HTTPS → port 443
  * DNS → port 53
* **Socket = IP + Port** → uniquely identifies a connection.

📌 **Analogy**:
Think of an **apartment building**: IP = building address, Port = flat number.

---

## APIs vs WebSockets

* **APIs (REST/HTTP)**:

  * Client sends a request, server replies.
  * Stateless, simple, widely used.
  * Example: `GET /weather?city=Delhi` → JSON response.

* **WebSockets**:

  * Full-duplex (two-way) communication.
  * Once connected, server can push data anytime.
  * Used for: chats, stock tickers, multiplayer games.

📌 **Analogy**:

* REST API → placing an **order at a restaurant** (one request → one response).
* WebSocket → having a **conversation with the waiter** throughout the meal.

---

## Summary

1. **TCP** reliable, **UDP** fast but unreliable, **QUIC** combines speed + security.
2. HTTP evolved from **simple GETs** to **HTTP/3 over QUIC**.
3. **Headers + caching** improve speed and efficiency.
4. **Status codes** help debug responses.
5. **Ports & sockets** identify processes.
6. **APIs vs WebSockets** → one-time request vs continuous conversation.

✅ Next, we’ll explore **Lesson 4 – Real-World Networking & Tools** (browser internals, DevTools, Wireshark, CLI, and code demos).
