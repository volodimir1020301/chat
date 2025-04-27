from socket import *
import threading
import time

def connect():
    while True:
        try:
            sock = socket(AF_INET, SOCK_STREAM)
            sock.connect(('6.tcp.eu.ngrok.io', 16426))
            name = input("Enter name: ")
            sock.send(name.encode())
            return sock
        except:
            print("Connection failed, retrying...")
            time.sleep(1)

client_socket = connect()

def send_message():
    while True:
        msg = input()
        if msg.lower() == 'exit':
            client_socket.close()
            break
        client_socket.send(msg.encode())

threading.Thread(target=send_message, daemon=True).start()

while True:
    try:
        message = client_socket.recv(1024).decode().strip()
        if message:
            print(message)
        else:
            break
    except:
        print("Disconnected")
        break