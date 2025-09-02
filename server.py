import socket
import threading

# Function to handle incoming messages
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Client: {message}")
            else:
                break
        except:
            break
    client_socket.close()

# Server setup
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5555))  # Bind to a specific address and port
    server.listen(5)  # Allow 5 connections at once
    print("Server listening on port 5555...")

    while True:
        client_socket, client_address = server.accept()
        print(f"New connection from {client_address}")
        
        # Start a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

# Start the server
if __name__ == "__main__":
    start_server()
