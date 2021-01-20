from socket import *
s=socket()
s.bind(('localhost',8888)) #FOR INTERNET USE IP ADDRESS OF MACHINE INSTEAD LOCATHOST
print("File Server is Listening")
s.listen()
path='D:\\abc\\sss.wmv'
f=open(path,'rb+')
c,addr=s.accept()
print("Client Connected",str(addr))
for line in f:
    c.send(line)
    print((line.__sizeof__()*100)/f.__sizeof__())


