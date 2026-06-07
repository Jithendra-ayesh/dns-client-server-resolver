import socket

HOST = "127.0.0.1"
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"[SERVER] Listening on {HOST}:{PORT}")

client_socket, client_address = server.accept()
print(f"[CONNECTED] {client_address}")

domain = client_socket.recv(1024).decode()

print(f"[REQUEST] {domain}")

try:
    ip_address = socket.gethostbyname(domain)

except socket.gaierror:
    ip_address = "Unable to resolve domain"

client_socket.send(ip_address.encode())
client_socket.close()
server.close()
