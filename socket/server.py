from socket import *

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 8080))
serverSock.listen()

connectionSock, addr = serverSock.accept()
print('connection from ', str(addr))

data = connectionSock.recv(1024)
print('data: ', data.decode('utf-8'))

connectionSock.send('I am a server'.encode('utf-8'))
print('message sent')
