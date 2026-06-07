import socket

HOST = "127.0.0.1"
PORT = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM
)

try:
    client.connect((HOST, PORT))

except ConnectionRefusedError:
    print("Unable to connect to server.")
    exit()

print("\n==============================")
print(" DNS Client")
print("==============================")

while True:
    query = input(
        "\nEnter domain or IP (type 'exit' to quit): "
    )

    if not query.strip():
        print("Please enter a domain or IP.")
        continue

    client.send(query.encode())

    if query.lower() == "exit":
        break

    response = client.recv(1024).decode()

    print(response)

print("\nDisconnected from server.")
client.close()
