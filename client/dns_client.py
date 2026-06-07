import socket

HOST = "127.0.0.1"
PORT = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM
)

client.connect((HOST, PORT))
print("\n==============================")
print(" DNS Client")
print("==============================")

while True:
    query = input(
        "\nEnter domain or IP (type 'exit' to quit): "
    )
    client.send(query.encode())

    if query.lower() == "exit":
        break
    response = client.recv(1024).decode()

    print(response)
client.close()
