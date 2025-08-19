from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))

serverSocket.listen(1)

print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f'Connection established with:, {addr}')

    message = connectionSocket.recv(2084).decode()
    print(f'Recieved message: {message}')

    recievedMessage = 'Server received: ' + message
    connectionSocket.send(recievedMessage.encode())

    connectionSocket.close()
    print('Connection closed')