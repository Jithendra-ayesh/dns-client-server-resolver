import socket
import threading

HOST = "127.0.0.1"
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"[SERVER] Listening on {HOST}:{PORT}")

def handle_client(client_socket, client_address):
    print(f"[CONNECTED] {client_address}")

    while True:
        query = client_socket.recv(1024).decode()

        if not query:
            break
        if query.lower() == "exit":
            break

        try:
            # Reverse Lookup
            if query.replace(".", "").isdigit():
                hostname = socket.gethostbyaddr(query)[0]
                response = f"{query} -> {hostname}"
            # Forward Lookup
            else:
                ip = socket.gethostbyname(query)
                response = f"{query} -> {ip}"

        except socket.herror:
            response = "No reverse DNS record found"

        except socket.gaierror:
            response = "Unable to resolve domain"

        except Exception as e:
            response = f"Error: {e}"

        client_socket.send(response.encode())
    client_socket.close()
    print(f"[DISCONNECTED] {client_address}")

while True:
    client_socket, client_address = server.accept()
    
    thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    thread.start()
