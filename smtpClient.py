from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Create a socket and establish a TCP connection with the mail server.
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    # Receive the server's greeting.
    recv = clientSocket.recv(1024).decode()

    # Send HELO command and receive server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.sendall(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()

    # Send MAIL FROM command and receive server response.
    mailFromCommand = 'MAIL FROM:<alice@example.com>\r\n'
    clientSocket.sendall(mailFromCommand.encode())
    recv2 = clientSocket.recv(1024).decode()

    # Send RCPT TO command and receive server response.
    rcptToCommand = 'RCPT TO:<bob@example.com>\r\n'
    clientSocket.sendall(rcptToCommand.encode())
    recv3 = clientSocket.recv(1024).decode()

    # Send DATA command and receive server response.
    dataCommand = 'DATA\r\n'
    clientSocket.sendall(dataCommand.encode())
    recv4 = clientSocket.recv(1024).decode()

    # Send the message data.
    clientSocket.sendall(msg.encode())

    # End the message with a single period and receive server response.
    clientSocket.sendall(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()

    # Send QUIT command and receive server response.
    quitCommand = 'QUIT\r\n'
    clientSocket.sendall(quitCommand.encode())
    recv6 = clientSocket.recv(1024).decode()

    clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
