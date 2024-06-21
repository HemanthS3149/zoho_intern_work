import threading
import socket
import time
from datetime import datetime
import random

class Server:
    def __init__(self, name):
        self.name = name
        self.lock = threading.Lock()
        self.total_clients = 0
        self.lost_clients = 0
        self.ratings = []
        self.current_clients = []
        self.start_date = datetime.now().date()

    def attend_client(self, client_name):
        with self.lock:
            if len(self.current_clients) < 3:  # Max number of clients that can be attended is 3
                self.current_clients.append(client_name)
                self.total_clients += 1
                print(f"{self.name} is attending {client_name}")  # Server will attend to client
                return True
            else:
                return False

    def finish_client(self, client_name, rating):
        with self.lock:
            if client_name in self.current_clients:
                self.current_clients.remove(client_name)
                self.ratings.append(rating)
                print(f"{client_name} finished chatting with {self.name} with rating {rating}")

    def get_average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)
    
    def log_activity(self):
        log_entry = (
            f"{datetime.now()} - {self.name} - Total Clients: {self.total_clients}, Lost Clients: {self.lost_clients}, "
            f"Average Rating: {self.get_average_rating():.2f}"
        )
        with open("archive.log", "a") as f:
            f.write(log_entry + "\n")
        # Log entry string is appended to archive.log, ensures that each log entry is added without overwriting

def start_server():
    host = '127.0.0.1'  # Localhost for local testing
    port = 65501
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    servers = [Server(f"Server {chr(65 + i)}") for i in range(3)]
    clients = []
    nicknames = []

    def broadcast(message):
        for client in clients:
            client.send(message)

    def handle(client, server_instance):
        while True:
            try:
                message = client.recv(1024).decode('ascii')
                if message.startswith("Rating:"):
                    rating = int(message.split(":")[1].strip())
                    nickname = nicknames[clients.index(client)]
                    server_instance.finish_client(nickname, rating)
                    client.close()
                    break
                else:
                    broadcast(message.encode('ascii'))
            except:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                server_instance.finish_client(nickname, random.randint(1, 5))
                broadcast(f"{nickname} left the chat!".encode('ascii'))
                nicknames.remove(nickname)
                break

    def receive():
        while True:
            client, address = server_socket.accept()
            print(f"Connected with {str(address)}")
            client.send("Nickname:".encode('ascii'))
            nickname = client.recv(1024).decode('ascii')
            nicknames.append(nickname)
            clients.append(client)

            assigned = False
            start_time = time.time()

            while time.time() - start_time < 300:  # 5 mins of waiting period
                for server_instance in servers:
                    if server_instance.attend_client(nickname):
                        client.send(f"Connected to {server_instance.name}".encode('ascii'))
                        broadcast(f"{nickname} joined the chat!".encode('ascii'))
                        thread = threading.Thread(target=handle, args=(client, server_instance))
                        thread.start()
                        assigned = True
                        break
                if assigned:
                    break
                time.sleep(1)

            if not assigned:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nicknames.remove(nickname)
                print(f"{nickname} could not be connected to any server")
                for server_instance in servers:
                    server_instance.lost_clients += 1

    print("Server is listening...")
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()
    return server_socket #We obtain a reference to the server socket object after it has been initialized and set up

server_socket = start_server()
