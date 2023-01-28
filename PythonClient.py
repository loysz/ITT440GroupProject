import socket

# define port and ip address of server
port = 8080
ip_address = "172.104.177.86"

# create Socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("\nSocket created")

# connect socket to 172.104.177.86 port 8080
client_socket.connect((ip_address, port))
print(f"Connected to {ip_address}") 

# input message to be send to server
request = input("Enter a message to send to the server: ")

# send encoded string to server
client_socket.send(request.encode())
print("Packet sent")

# print incoming reply from server
response = client_socket.recv(1024).decode()
print(f"Server response: {response}")

# close socket
client_socket.close()
print("Disconnected\n")
