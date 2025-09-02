import socket
import threading

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Server: {message}")
            else:
                break
        except:
            break

# Function to send messages to the server
def send_messages(client_socket):
    while True:
        message = input("You: ")
        if message:
            client_socket.send(message.encode('utf-8'))

# Client setup
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5555))  # Connect to the server

    # Start threads for receiving and sending messages
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    send_thread = threading.Thread(target=send_messages, args=(client,))

    receive_thread.start()
    send_thread.start()

# Start the client
if __name__ == "__main__":
    start_client()
