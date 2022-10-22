import socket
import time

host_name = "localhost"
port = 8080

network_socket = socket.socket()
network_socket.bind((host_name,port))

network_socket.listen(1)

connection , address = network_socket.accept()
print(str(connection)+"sucssess connection")

while True:
    while True:
        try:
            get_data = str(connection.recv(1024).decode())
            print("Client send to :"+ get_data)
            break
        except ConnectionAbortedError:
            time.sleep(2)
            print(str(connection)+"sucssess connection")
    if get_data == "end":
        break
    else:
        message = input("----:")
        print("weaitting for client...")
        connection.send(message.encode())
