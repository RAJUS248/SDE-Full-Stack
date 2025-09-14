import socket
c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
c.sendto(b"Namaskara Karantaka!", ("127.0.0.1", 9999))
print(c.recvfrom(2048))