# client side of the socket connection
import socket

# SOCK_STREAM is the TCP type of socket, SOCK_DGRAM is the UDP type of socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(socket.gethostname())
client_socket.connect((socket.gethostbyname(socket.gethostname()), 12344))



while True:
    message = client_socket.recv(1024).decode("utf-8")
    print(message)
    
    if message == "quit":
        client_socket.send(bytes("Dooooi", "utf-8"))
        client_socket.send(bytes("quit", "utf-8"))
        print("Closing connection")
        break
    
    my_msg = input("Enter your message: ")
    client_socket.send(bytes(my_msg, "utf-8"))
    
client_socket.close()
