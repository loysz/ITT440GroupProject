import socket
import threading

# data handler function
def handle_client(client_socket):
    global threadcount
    # decode the incoming packer
    request = client_socket.recv(1024).decode()

    # manipulate incoming text 
    response = request + " from server xyz"

    # return encoded combined string to client
    client_socket.send(response.encode())
    print(f"[*] Responded to {client_address[0]}:{client_address[1]}")

    # close socket
    client_socket.close()
    print(f"[*] Disconnected from {client_address[0]}:{client_address[1]}")
    threadcount -= 1
    print(f"[*] Active thread:{str(threadcount)}")

# create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"\n[*] Socket created")

# define port
port = 8080

# bind socket to port
server_socket.bind(("0.0.0.0", port))
print(f"[*] Successfully bind to port:{str(port)}")

# listen for incoming connection (max 5 connection in a queue)
server_socket.listen(5)
print("[*] Waiting for client")

# define threadcount
threadcount = 0

# accept connection
while True:
    client_socket, client_address = server_socket.accept()
    print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")
    threadcount += 1
    print(f"[*] Active thread:{str(threadcount)}")

    # fork and multithread
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
