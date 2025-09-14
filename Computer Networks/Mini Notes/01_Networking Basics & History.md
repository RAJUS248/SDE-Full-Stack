
# 📘 Lesson 1 – Networking Basics & History

## 📑 Index

1. [ARPANET & TCP/IP History](#arpanet--tcpip-history)
2. [Signal Transmission (Copper, Fiber, Wireless)](#signal-transmission-copper-fiber-wireless)
3. [MAC Addressing & NIC](#mac-addressing--nic)
4. [Packet Switching & Data Encoding](#packet-switching--data-encoding)
5. [Summary](#summary)

---

## ARPANET & TCP/IP History

* In the **1960s**, the U.S. Department of Defense’s ARPA created **ARPANET**, the first computer network.
* It introduced **packet switching** — instead of reserving a full line like telephone calls (circuit switching), data was sent in small “packets.”
* ARPANET also had a **decentralized design** (no single failure point), important during the Cold War.

🔑 **Fun fact**: The very first message sent in 1969 was “LO” (meant to be LOGIN) before the system crashed.

* In the **1980s**, the **TCP/IP protocol suite** became the global standard, connecting different networks into one Internet.
* **Vint Cerf** and **Bob Kahn** are called the “fathers of the Internet” for their work on TCP/IP.
* In the **1990s**, **Tim Berners-Lee** invented the **World Wide Web (HTTP + HTML)** → first websites, browsers.

📌 **Analogy**:
Think of TCP/IP as a **universal language** that allows computers worldwide to talk to each other, just like English helps people from different countries communicate.

---

## Signal Transmission (Copper, Fiber, Wireless)

Data moves as **signals** through different media:

### 1. Copper Cables (Ethernet)

* Uses **electrical voltage pulses** to represent 0s and 1s.
* Wires are twisted (Cat5e, Cat6) to reduce interference.
* **Encoding methods**:

  * **NRZ**: high voltage = 1, low = 0.
  * **Manchester encoding**: change in voltage in the middle of each bit for synchronization.

📌 **Analogy**: Like sending **Morse code signals** over a wire, but faster and automated.

---

### 2. Optical Fiber

* Sends data as **light pulses** through glass strands.
* **Laser/LED** converts electrical signals → light.
* Advantages: very high speed, long distances, no electrical interference.
* Used in **undersea cables** to connect continents.

📌 **Analogy**: Like sending messages with **flashlights** through a clear tunnel.

---

### 3. Wireless (Wi-Fi, Cellular)

* Uses **radio waves** via antennas.
* Standards: Wi-Fi (IEEE 802.11), 4G/LTE, 5G.
* Pros: mobility, convenience.
* Cons: interference, lower speed vs fiber.

📌 **Analogy**: Like talking on a **walkie-talkie** — you don’t need wires, but signals can get noisy.

---

## MAC Addressing & NIC

* Every device has a **Network Interface Card (NIC)** → Ethernet adapter or Wi-Fi chip.
* Each NIC has a **MAC address** (unique 48-bit hardware ID, e.g., `00:1A:2B:3C:4D:5E`).
* Used for **local network communication** (LAN).

📌 **How it works**:

* Your laptop → sends data → frames it with the destination MAC.
* Switch → forwards it only to the correct device (like a postman reading house numbers).
* **ARP (Address Resolution Protocol)**: finds which MAC belongs to which IP (like a phonebook).

---

## Packet Switching & Data Encoding

### Circuit Switching (Old Telephony)

* A **dedicated line** for the entire call.
* Example: landline phones.

### Packet Switching (Internet)

* Breaks data into **small packets** (\~1500 bytes).
* Each packet has: source, destination, sequence number.
* Packets may take **different routes**, then get reassembled at the destination.

📌 **Analogy**:
Think of sending a **book by courier** — instead of shipping the whole book at once, you send it **page by page** in different trucks. At the destination, pages are reassembled.

---

### Data Encoding

* **Copper**: Voltage changes (NRZ, Manchester).
* **Fiber**: Light pulses (1 = light, 0 = no light).
* **Wireless**: Radio wave modulation (AM, FM, QAM).

📌 **Analogy**: Encoding is like deciding on a **secret code**:

* Thumbs up = “yes,” thumbs down = “no.”
* Both sender and receiver must agree on the code.

---

## Summary

1. **ARPANET** → birth of networking, **TCP/IP** became global standard.
2. **Transmission media**: copper (electric), fiber (light), wireless (radio).
3. **MAC address + NIC**: unique device IDs for local communication.
4. **Packet switching**: efficient, resilient way to send data.
5. **Encoding**: methods to convert 0s and 1s into real-world signals.
