
# 📘 Lesson 4 – Real-World Networking & Tools

## 📑 Index

1. [Browser Behavior (DOM, Rendering, Caching)](#browser-behavior-dom-rendering-caching)
2. [DevTools: Inspecting Requests & Responses](#devtools-inspecting-requests--responses)
3. [Wireshark & Packet Analysis](#wireshark--packet-analysis)
4. [CLI Tools: curl, dig, traceroute](#cli-tools-curl-dig-traceroute)
5. [Code Demos in Python, Java, and C](#code-demos-in-python-java-and-c)
6. [Summary](#summary)

---

## Browser Behavior (DOM, Rendering, Caching)

When you visit a website, the browser does a lot of work behind the scenes:

1. **Parse HTML** → builds the **DOM (Document Object Model)** tree.
2. **Download CSS & JS** → builds CSSOM and applies styles.
3. **Render Tree** → combines DOM + CSSOM for layout.
4. **Painting** → converts elements into pixels on screen.
5. **JavaScript execution** → modifies DOM, handles events.
6. **Caching** → stores files locally for faster reloads.

📌 **Analogy**:
It’s like cooking a dish:

* Recipe = HTML, Spices = CSS, Cooking steps = JS, Final dish = rendered page.

---

## DevTools: Inspecting Requests & Responses

Modern browsers (Chrome, Firefox, Edge) have **Developer Tools**.

* **Network Tab** → see every HTTP request: URL, status code, response time, headers, size.
* **Console Tab** → logs, errors, JS debugging.
* **Application Tab** → cookies, local storage, service workers.

📌 **Why useful?**

* Helps debug slow loading pages.
* Shows caching rules in action.
* Displays redirects (301, 302).

---

## Wireshark & Packet Analysis

**Wireshark** = most popular packet sniffer.

* Captures all packets going through your NIC.
* Can filter by protocol: `http`, `tcp.port==443`, `dns`.
* Shows packet headers and payloads.
* Useful for learning and troubleshooting.

📌 **Example**: Capture DNS traffic when opening `google.com`:

* Request: `Standard query A google.com`
* Response: `142.250.190.78`

📌 **Analogy**:
Like being an **airport security scanner** — you see every bag (packet), where it came from, and what’s inside.

---

## CLI Tools: curl, dig, traceroute

### 🔹 curl

* Used to send HTTP requests from terminal.

```bash
curl -I https://www.google.com
```

* `-I` → only fetch headers.

### 🔹 dig

* Query DNS records.

```bash
dig google.com
```

### 🔹 traceroute (Linux/macOS) / tracert (Windows)

* Shows hops a packet takes to reach destination.

```bash
traceroute google.com
```

📌 **Analogy**:
These tools are like having **X-ray glasses** for networking — you see exactly how requests flow.

---

## Code Demos in Python, Java, and C

### Python: Simple HTTP GET

```python
import requests

response = requests.get("https://www.google.com")
print("Status:", response.status_code)
print("First 100 chars:", response.text[:100])
```

---

### Java: Using HttpURLConnection

```java
import java.net.*;
import java.io.*;

public class SimpleHttp {
    public static void main(String[] args) throws Exception {
        URL url = new URL("https://www.google.com");
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("GET");

        System.out.println("Status: " + conn.getResponseCode());

        BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        String line;
        while ((line = in.readLine()) != null) {
            System.out.println(line);
        }
        in.close();
    }
}
```

---

### C: Basic Socket Example

```c
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <netdb.h>
#include <unistd.h>

int main() {
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    struct hostent *server = gethostbyname("www.google.com");

    struct sockaddr_in server_addr;
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(80);
    memcpy(&server_addr.sin_addr.s_addr, server->h_addr, server->h_length);

    connect(sock, (struct sockaddr *)&server_addr, sizeof(server_addr));
    char *msg = "GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n";
    send(sock, msg, strlen(msg), 0);

    char buffer[1024];
    int n = read(sock, buffer, 1023);
    buffer[n] = '\0';
    printf("%s\n", buffer);

    close(sock);
    return 0;
}
```

📌 **Note**: The Python example is simplest; Java and C show how deeper control is possible.

---

## Summary

1. Browsers build **DOM + CSSOM → Render Tree → Painted page**.
2. **DevTools** let you inspect requests, headers, cache.
3. **Wireshark** shows raw packet data for deep troubleshooting.
4. **CLI tools** like `curl`, `dig`, `traceroute` help test connectivity.
5. **Code demos** show how apps send HTTP requests in Python, Java, C.
