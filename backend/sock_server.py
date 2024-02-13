# server side of the socket connection
import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((socket.gethostbyname(socket.gethostname()), 12344))
server_socket.listen()

client_socket, address = server_socket.accept()
print(f"Connection from {address} has been established!")
client_socket.send(bytes("Hey welcome to myyy server!", "utf-8"))

while True:
    client_message = client_socket.recv(1024).decode("utf-8")
    print(client_message)
    
    if client_message  == "quit":
        client_socket.send(bytes("quit", "utf-8"))
        print("Closing connection")
        break
    
    my_msg = input("Enter your message: ")
    client_socket.send(bytes(my_msg, "utf-8"))


client_socket.close()
