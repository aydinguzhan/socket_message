import socket
import time

host_name = "localhost"
port = 8080

network_socket = socket.socket()
network_socket.connect((host_name,port))


print(f"Connection sucsses! {host_name}:{port}")

message = input("----:")
print("waiting for server...")

while message != "end":
    network_socket.send(message.encode())
    get_data = network_socket.recv(1024).decode()

    print("Server : "+ get_data)

    message = input("----:")
    print("waiting for server...")

network_socket.close()
