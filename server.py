from socket import *
from threading import Thread

names=[]
clients=[]
s = socket(AF_INET, SOCK_STREAM)
s.bind(('localhost',9999))
print("Server has been started...")
s.listen()
print("Waiting for connection...")
def broadcast(msg):
    for client in clients:
        client.send(msg)
def handle(client):
    while True:
        try:
            msg=client.recv(1024)
            broadcast(msg)
        except:
            index=clients.index(client)
            clients.remove(client)
            client.close()
            name=names[index]
            broadcast(f'{name} left the chat!'.encode('ascii'))
            names.remove(name)
            break
def recive():
    while True:
        c,addr=s.accept()
        print(f"Connected with {str(addr)}")
        c.send("name".encode('ascii'))
        name=c.recv(1024).decode('ascii')
        names.append(name)
        clients.append(c)
        print("Client name is",name)
        broadcast(f'{name} joined the chat'.encode('ascii'))
        c.send("\nconnected to the server".encode("ascii"))
        thread=Thread(target=handle,args=(c,))
        thread.start()

recive()