from socket import *
import threading
import time


def send(sock):
    while True:
        sendData = input('>>>')
        sock.sendall(sendData.encode('utf-8'))


def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print('opponent: ', recvData.decode('utf-8'))


port = 8080

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSock.bind(('', port))

serverSock.listen(1)

connectionSock, addr = serverSock.accept()

sender = threading.Thread(target=send, args=(connectionSock,))
receiver = threading.Thread(target=receive, args=(connectionSock, ))

sender.start()
receiver.start()

while True:
    time.sleep(1)
