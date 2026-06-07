import socket
import threading
from datetime import datetime

HOST = "0.0.0.0"
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"[SERVER] Listening on {HOST}:{PORT}")

def log_query(client_ip, query, response):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    with open("results.txt", "a") as file:

        file.write(
            f"\n[{timestamp}]\n"
            f"Client IP : {client_ip}\n"
            f"Query     : {query}\n"
            f"Response  : {response}\n"
            f"{'-'*40}\n"
        )

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

        log_query(client_address[0], query, response)
        client_socket.send(response.encode())
    client_socket.close()
    print(f"[DISCONNECTED] {client_address}")

while True:
    client_socket, client_address = server.accept()
    
    thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    thread.start()
