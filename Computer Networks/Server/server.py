import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 9999))
print("UDP server on :9999")
while True:
    data, addr = s.recvfrom(2048)
    print("from", addr, ":", data.decode())
    s.sendto(b"ack:"+data, addr)