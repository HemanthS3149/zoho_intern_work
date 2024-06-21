import socket
import threading
from datetime import datetime

nickname = input('Enter a nickname: ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creates a new TCP socket obj
client.connect(('127.0.0.1', 65501))

#defining global var to store server name
server_name=None#we have to obtain this val

def receive():
    global server_name
    while True: #to continuosly receive messages
        try:
            message = client.recv(1024).decode('ascii')
            if message.startswith("Connected to"):
                server_name=message.split()[3] #this will give us server name
            elif message == "Nickname:":
                client.send(nickname.encode('ascii'))
            elif "Rating:" in message:
                while True:
                    try:
                        rating = int(input("Rate the server from 1 to 5: "))
                        if 1 <= rating <= 5:
                            client.send(f"Rating: {rating}".encode('ascii'))
                            client.close()
                            break
                        else:
                            print("Rating must be between 1 and 5.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                break
            else:
                print(message)
        except ConnectionResetError:
            print("Connection to server was reset.")
            client.close()
            break
        except ConnectionAbortedError:
            print("Connection to server was aborted.")
            client.close()
            break
        except:
            print("An error has occurred.")
            client.close()
            break

def write():
    while True:
        try:
            message = input("")
            full_message = f"{nickname} ({datetime.now()}): {message}  (Server: {server_name})"
            client.send(full_message.encode('ascii'))
        except ConnectionResetError:
            print("Connection to server was reset.")
            client.close()
            break
        except ConnectionAbortedError:
            print("Connection to server was aborted.")
            client.close()
            break
        except:
            print("An error has occurred.")
            client.close()
            break

receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()
