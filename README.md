# Python Client-Server Application

This is a simple Python client-server application that demonstrates how to establish a socket connection between a client and a server, send messages from the client to the server, and receive responses from the server.

## Prerequisites

Before running the code, make sure you have the following:

- Python installed on your system.
- Basic understanding of networking concepts.

## Files

- `PythonClient.py`: The client-side code that connects to the server and sends messages.
- `PythonServer.py`: The server-side code that listens for incoming connections, processes messages, and responds to clients.

## Usage

1. Start the server:
   - Run `PythonServer.py` on the computer that will act as the server. The server will start listening on port 8080.

2. Start the client:
   - Run `PythonClient.py` on the computer that will act as the client.
   - You will be prompted to enter a message to send to the server.

3. Client-Server Communication:
   - The client will establish a connection with the server using the specified IP address and port.
   - The client will send the message to the server, and the server will receive and process it.
   - The server appends " from server xyz" to the received message and sends it back to the client.
   - The client displays the server's response.

4. Terminate the server:
   - You can terminate the server by pressing `Ctrl+C` in the terminal where it is running.

## Customize

- You can modify the `port` and `ip_address` in the client code to match your server's configuration.
- Customize the message handling logic in the `handle_client` function in the server code to perform the desired operations.
