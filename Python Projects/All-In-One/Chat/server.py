import socket
import threading

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        self.connection, self.address = self.server_socket.accept()
        print(f"Connected by {self.address}")

    def receive_message(self):
        while True:
            message = self.connection.recv(1024).decode()
            if not message:
                break
            print(f"Received message: {message}")

    def send_message(self):
        while True:
            message = input("Server: ")
            if message.lower() == 'quit':
                break
            self.connection.sendall(message.encode())

    def start(self):
        receive_thread = threading.Thread(target=self.receive_message)
        send_thread = threading.Thread(target=self.send_message)
        receive_thread.start()
        send_thread.start()

if __name__ == "__main__":
    server = Server('127.0.0.1', 5000)
    server.start()
