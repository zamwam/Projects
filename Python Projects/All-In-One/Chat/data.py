import socket
import threading

class Host:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        print("Connected to server. Type 'quit' to exit.")

    def receive_message(self):
        while True:
            message = self.client_socket.recv(1024).decode()
            if not message:
                break
            print(f"Server: {message}")

    def send_message(self):
        while True:
            message = input("You: ")
            if message.lower() == 'quit':
                break
            self.client_socket.sendall(message.encode())

    def start(self):
        receive_thread = threading.Thread(target=self.receive_message)
        send_thread = threading.Thread(target=self.send_message)
        receive_thread.start()
        send_thread.start()

if __name__ == "__main__":
    host = Host('127.0.0.1', 5000)
    host.start()