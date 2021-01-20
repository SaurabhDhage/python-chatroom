from socket import *
from threading import Thread
c=socket(AF_INET,SOCK_STREAM)
c.connect(('127.0.0.1',9999))
name=input("Enter the name:")
def recive():
    while True:
        try:
            msg=c.recv(1024).decode('ascii')
            if msg=='name':
                c.send(name.encode())
            else:
                print(msg)
        except:
            print("An Error Occured")
            c.close()
            break
def write():
    while True:
        msg=f'{name}:{input()}'
        c.send(msg.encode('ascii'))

t1=Thread(target=recive)
t2=Thread(target=write)
t1.start()
t2.start()