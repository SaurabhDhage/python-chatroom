from socket import socket
c=socket()
c.connect(('127.0.0.1',8888))
f=open("D:\\AJP\\img.jpg",'wb')
while True:
    line = c.recv(1024)
    if line!=''.encode():
        f.write(line)
    else:
        break
    print(line)