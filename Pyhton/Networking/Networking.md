# Networking Interview Notes for MAANG/FAANG Freshers

---

## 1. Networking Fundamentals

### What is Networking?
Networking is the practice of connecting multiple computers or devices together so they can communicate, share data, and access resources such as files, printers, and internet connections. It forms the backbone of modern computing, enabling everything from web browsing to cloud computing.

---

## 2. Key Protocols & Their Differences

Understanding protocols is essential as they define the rules and conventions for communication between network devices. Here are the core protocols you should know:

| Protocol    | Layer (OSI Model)  | Purpose                                 | Advantages                            | Disadvantages                   |
|-------------|--------------------|-----------------------------------------|-------------------------------------|--------------------------------|
| **TCP**     | Transport (Layer 4) | Reliable, connection-oriented data transfer | Ensures ordered delivery, error correction, and retransmission of lost packets | More overhead and latency compared to UDP |
| **UDP**     | Transport          | Connectionless, faster data transfer    | Low latency, efficient for real-time applications | No guarantee of delivery or order |
| **HTTP**    | Application (Layer 7) | Protocol for transferring hypertext (web pages) | Widely used, simple, stateless     | No encryption in plain HTTP    |
| **HTTPS**   | Application        | Secure version of HTTP using TLS/SSL    | Encrypts data in transit, protects user privacy | Slightly slower due to encryption overhead |
| **FTP**     | Application        | File Transfer Protocol                   | Allows uploading/downloading files | Does not encrypt data, insecure |
| **DNS**     | Application        | Domain Name System - converts domain names to IP addresses | Makes internet human-friendly      | Vulnerable to spoofing and attacks |
| **IP**      | Network (Layer 3)  | Internet Protocol for addressing and routing packets | Universal standard, enables routing across networks | Unreliable delivery, no error correction |
| **ICMP**    | Network            | Internet Control Message Protocol for diagnostics and error reporting | Useful for troubleshooting (ping, traceroute) | Not meant for data transfer   |
| **ARP**     | Data Link (Layer 2) | Resolves IP addresses to MAC addresses on local networks | Enables device discovery on LAN    | Only works within the same subnet |
| **DHCP**    | Application        | Dynamic Host Configuration Protocol - automatically assigns IP addresses | Simplifies network management       | Can be a security risk if compromised |

### Explanation:
- **TCP vs UDP:** TCP is like a phone call (guaranteed delivery), UDP is like a walkie-talkie (best effort, no guarantee).
- **HTTP vs HTTPS:** HTTPS uses encryption to secure web data.
- **DNS:** Acts as the internet's phone book, converting easy-to-remember domain names to numeric IP addresses computers understand.
- **IP:** Core addressing system allowing packets to find their destination across networks.
- **ICMP:** Used by tools like `ping` to check connectivity.
- **ARP:** Translates IP addresses to hardware addresses (MAC) on local networks.
- **DHCP:** Automatically assigns IPs to devices joining a network, reducing manual setup.

---

## 3. How the Internet Works (Simplified)

The internet is a massive network of interconnected computers. Here's a simplified flow of how it works:

1. **IP Addressing:** Every device connected to the internet has a unique IP address.
2. **DNS Resolution:** When you type a URL, DNS servers convert the domain (like google.com) into an IP address.
3. **Routing:** Routers pass your data packets through multiple networks to reach the destination server.
4. **Packet Switching:** Data is broken into small chunks (packets) and sent independently over the best available path.
5. **Protocols:** TCP ensures reliable delivery, UDP enables fast but unreliable communication.
6. **Internet Service Providers (ISP):** ISPs connect you to the larger internet backbone.
7. **Response:** The server sends the requested data back through the network using the same protocols.

### Example:
When you open `www.example.com`:
- Your computer asks a DNS server for the IP.
- Your browser establishes a TCP connection with that IP.
- Sends an HTTP request.
- Server responds with the web page data.
- Browser renders the page.

---

## 4. How Browsers Work

Browsers are complex software that enable you to access and interact with web pages. Here's an overview of the process:

1. **URL Input & DNS Lookup:** You enter a URL → Browser queries DNS to get the IP.
2. **TCP Handshake:** Browser establishes a TCP connection with the server.
3. **HTTP Request:** Browser sends an HTTP request (GET, POST, etc.).
4. **Server Response:** Server sends back HTML, CSS, JavaScript, and media.
5. **Parsing & Rendering:**
   - **HTML Parser:** Builds the DOM (Document Object Model) tree.
   - **CSS Parser:** Builds CSSOM tree.
   - **Render Tree:** Combines DOM & CSSOM to know how to paint the page.
6. **JavaScript Engine:** Executes JavaScript code, modifies DOM/CSSOM dynamically.
7. **Layout & Paint:** Browser calculates layout and paints pixels on screen.
8. **User Interaction:** Browser handles events like clicks and inputs.

---

## 5. How Web Servers Work

Web servers listen for client requests and serve content:

- **Listening:** Servers listen on ports (80 for HTTP, 443 for HTTPS).
- **Request Handling:** Receive HTTP requests, may run backend logic or serve static files.
- **Response Generation:** Sends HTML, JSON, images, etc. with an HTTP status code.
- **Status Codes:** Indicate success (200), redirects (301), errors (404, 500).
- **Optimization:** Servers use caching, compression, and keep-alive connections for speed.

### Example:
A web server like Apache or Nginx waits for requests. When a user requests a page, it either serves the file directly or forwards to an application server.

---

## 6. How APIs Work

APIs allow communication between different software systems:

- **Definition:** APIs define a set of rules to exchange data and invoke functionalities.
- **REST APIs:** Use HTTP methods (GET, POST, PUT, DELETE) for CRUD operations.
- **Data Format:** Usually JSON or XML.
- **Stateless:** Each API request is independent.
- **Authentication:** API keys, OAuth tokens protect access.
- **Example:** A weather app uses a REST API to get data from a weather server.

---

## 7. How JavaScript Engine Works in Browser

JavaScript engines execute JS code in browsers, enabling interactivity:

- **Parsing:** JavaScript source code is parsed into an Abstract Syntax Tree (AST).
- **Compilation:** Engines like V8 (Chrome) use Just-In-Time (JIT) compilation to convert JS to optimized machine code.
- **Execution:** Runs the compiled code, managing scope, closures, and events.
- **Garbage Collection:** Automatically frees memory used by unreachable objects.
- **Event Loop:** Handles asynchronous operations (timers, network calls) without blocking UI.

---

## 8. Important System Components

### Load Balancer
- Distributes incoming network or application traffic across multiple servers.
- **Types:** Round Robin, Least Connections, IP Hash.
- **Benefits:** Prevents overload, improves reliability, supports scalability.
- **Example:** Large websites use load balancers to spread traffic evenly.

### Frontend Systems
- The part users interact with (browsers, UI frameworks).
- Responsible for rendering UI, handling user input, and running client-side logic.

### DNS (Domain Name System)
- A hierarchical, distributed naming system for computers.
- Converts domain names to IP addresses.
- Involves recursive resolvers and authoritative name servers.
- Uses caching to improve speed.
- Vulnerable to spoofing and cache poisoning attacks, mitigated via DNSSEC.

---

## 9. Security Topics

### DoS (Denial of Service) Attack
- An attack aiming to make a service unavailable by overwhelming it with traffic.
- Types:
  - **Flood Attack:** Sending massive requests.
  - **Amplification Attack:** Exploiting vulnerable systems to send large volumes of traffic.
- **Mitigations:** Firewalls, traffic filtering, rate limiting, and distributed mitigation (DDoS protection).

### Rate Limiter
- Controls the number of requests a user can make in a given time window.
- Prevents abuse and protects resources.
- Common algorithms:
  - **Token Bucket:** Tokens added at a fixed rate, requests consume tokens.
  - **Leaky Bucket:** Requests added to a queue that leaks at a fixed rate.

---

## 10. Summary Table: Protocols & Concepts

| Concept           | Key Points                                               | Use Case Example                |
|-------------------|----------------------------------------------------------|--------------------------------|
| TCP               | Reliable, ordered, connection-oriented                   | Web browsing, email delivery   |
| UDP               | Fast, connectionless, no reliability guarantee           | Video streaming, online games  |
| HTTP / HTTPS      | Web page transfer, HTTPS adds encryption                  | Accessing websites securely    |
| DNS               | Domain name to IP translation                             | Accessing `google.com`          |
| Load Balancer     | Distributes traffic across servers                        | Scaling high-traffic websites  |
| DoS Attack        | Floods a service to make it unavailable                   | Attacks on online platforms    |
| Rate Limiter      | Limits client requests to prevent abuse                   | API protection                 |
| JavaScript Engine | Executes JS, handles async, JIT compilation               | Browser interactivity          |
| API               | Software communication interface                          | Mobile apps accessing servers  |

---

# Additional Resources

- **Books:** "Computer Networking: A Top-Down Approach" by Kurose and Ross
- **Websites:** MDN Web Docs (networking and web API sections), official protocol RFCs
- **Practice:** Implement simple client-server apps, experiment with curl and Postman for APIs

---

*Good luck with your interviews! Feel free to ask if you want me to prepare examples, coding tasks, or system design questions on networking.*

