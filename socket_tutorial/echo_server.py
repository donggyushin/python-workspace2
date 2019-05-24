import socket
import threading


def server():
    host = ''
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    while True:
        listeningForClient(server_socket)


def echo(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.send(data)
    conn.close()


def listeningForClient(server_socket):
    conn, address = server_socket.accept()
    t = threading.Thread(target=echo, args=(conn,))
    t.start()


if __name__ == '__main__':
    server()
