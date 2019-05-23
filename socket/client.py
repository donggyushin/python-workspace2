from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 8080))

print("connection complete")

clientSock.send('I am a client'.encode('utf-8'))

print('message sent')

data = clientSock.recv(1024)
print('data: ', data.decode('utf-8'))
