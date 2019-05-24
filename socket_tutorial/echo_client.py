import socket


def client():
    host = 'localhost'
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    data = input('data to send:')

    while data.lower().strip() != 'quit()':
        client_socket.send(data.encode())
        received_data = client_socket.recv(1024).decode()

        print('Received from server: ', received_data)
        data = input('data to send:')
    client_socket.close()


if __name__ == "__main__":
    client()
