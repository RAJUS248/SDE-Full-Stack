
# 📘 Lesson 2 – Core Internet Protocols & Data Journey

## 📑 Index

1. [IP, NAT, DHCP, DNS, Routing (BGP, TTL)](#ip-nat-dhcp-dns-routing-bgp-ttl)
2. [Anatomy of a Packet](#anatomy-of-a-packet)
3. [End-to-End Journey: Client to Server and Back](#end-to-end-journey-client-to-server-and-back)
4. [Example: What Happens When You Type google.com](#example-what-happens-when-you-type-googlecom)
5. [Summary](#summary)

---

## IP, NAT, DHCP, DNS, Routing (BGP, TTL)

### 🌐 Internet Protocol (IP)

* IP gives each device a **unique address** (like a postal address).
* Versions:

  * **IPv4** → 32-bit (\~4.3 billion addresses). Almost exhausted.
  * **IPv6** → 128-bit (virtually unlimited).
* IP is **connectionless**: it just sends packets without guaranteeing delivery.

📌 **Analogy**:
Sending a postcard → you write the destination, drop it in a box, but delivery is not guaranteed.

---

### 🖥 DHCP (Dynamic Host Configuration Protocol)

* Automates giving devices an IP address when they connect.
* Your router acts as a **DHCP server**: assigns IP, subnet mask, gateway, DNS.

📌 **Analogy**:
Like checking into a hotel → receptionist (DHCP) assigns you a **room number (IP)** and tells you the **Wi-Fi password (DNS, gateway)**.

---

### 📖 DNS (Domain Name System)

* Translates domain names (google.com) → IP addresses (142.250.190.78).
* Works like an **Internet phonebook**.
* Query goes step by step:

  * Root servers → Top-level domain (.com) → Google’s authoritative DNS → IP returned.

📌 **Analogy**:
Instead of remembering every person’s **phone number**, you look them up in a **directory**.

---

### 🔄 NAT (Network Address Translation)

* Allows many devices in a home/office to share **one public IP**.
* Router changes private IP (e.g., `192.168.0.5`) into a single public IP for the Internet.

📌 **Analogy**:
Like an office receptionist → employees have **extensions (private IPs)**, but outsiders only know the **main office number (public IP)**.

---

### 🚦 Routing & BGP (Border Gateway Protocol)

* Routers move packets hop by hop using **routing tables**.
* BGP connects different ISPs and large networks → decides the **best path** globally.
* IP packets carry **TTL (Time to Live)** → decreases at each hop; prevents infinite loops.

📌 **Analogy**:
Like **Google Maps** for the Internet: routers exchange routes and forward packets along the fastest/available path.

---

## Anatomy of a Packet

When data is sent, it’s wrapped in multiple “envelopes” (headers).

```
+--------------------------------------------------+
| Ethernet Frame                                   |
|  +--------------------------------------------+  |
|  |   IP Packet                                |  |
|  |    +------------------------------------+  |  |
|  |    |   TCP Segment                       |  |  |
|  |    |     +----------------------------+ |  |  |
|  |    |     |   HTTP Data (or TLS if HTTPS)| |  |  |
|  |    |     +----------------------------+ |  |  |
|  |    +------------------------------------+  |  |
|  +--------------------------------------------+  |
+--------------------------------------------------+
```

* **Layer 2 (Ethernet/Wi-Fi)** → MAC addresses.
* **Layer 3 (IP)** → Source/Destination IP, TTL.
* **Layer 4 (TCP/UDP)** → Ports, sequence numbers.
* **Layer 7 (Application)** → HTTP request/response.

📌 **Analogy**:
Like a **Russian doll** — each smaller doll is wrapped inside a bigger one, until only the outer doll is visible.

---

## End-to-End Journey: Client to Server and Back

1. **DNS Resolution** → Browser asks for server IP.
2. **TCP Handshake** → SYN → SYN-ACK → ACK (connection set).
3. **TLS Handshake** (if HTTPS) → secure keys exchanged.
4. **Request Travels** → Packet goes through NAT, ISP, undersea cables, etc.
5. **Routers Use TTL** → ensures no endless loops.
6. **Server Handling** → Load balancer, firewall, then application server.
7. **Response Back** → travels back via routing, NAT translates it, arrives at laptop.
8. **Browser Renders** → OS reassembles packets, browser displays page.

📌 **Analogy**:
It’s like ordering food:

* You ask (DNS).
* Restaurant confirms your order (handshake).
* Delivery happens via multiple roads (routing).
* Food arrives in parts (packets) and is reassembled into a full meal.

---

## Example: What Happens When You Type google.com

1. Laptop gets IP via **DHCP**.
2. Browser does a **DNS lookup** for `google.com`.
3. Browser opens a **TCP connection** to Google’s IP (port 443).
4. **TLS handshake** secures the channel.
5. Browser sends an **HTTP GET request**.
6. Google server replies with **HTTP 200 OK + HTML page**.
7. Browser renders HTML, loads CSS, JS, images.
8. On repeat visits: caching + persistent connections = faster.

📌 **Analogy**:
Typing google.com is like **visiting a library**:

* First, you ask the librarian (DNS) where the book is.
* Then you reserve a study desk (TCP connection).
* You show your ID for access (TLS).
* Finally, you get the book (HTTP response).

---

## Summary

1. **IP** → addresses, **DNS** → name resolution.
2. **DHCP** → automatic IP configuration.
3. **NAT** → multiple devices share one public IP.
4. **Routing & BGP** → best path for packets, **TTL** avoids loops.
5. **Packets** → layered like envelopes.
6. **End-to-end journey** → DNS → TCP → TLS → HTTP → Browser render.
7. Example google.com → shows all steps together.
