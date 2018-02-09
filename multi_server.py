import socket
import select

PORT = 1025
HOME = '0.0.0.0'

server_socket = socket.socket()
server_socket.bind((HOME, PORT))

server_socket.listen(5)
open_client_sockets = []
messages_to_send = []


def send_waiting_messages(wlist):
    for message in messages_to_send:
        (client_socket, data1) = message
        print data1
        for socket1 in wlist:
            if socket1 != client_socket:
                socket1.send(data1)
        messages_to_send.remove(message)


def server_cycle():
    while True:
        rlist, wlist, xlist = select.select([server_socket] + open_client_sockets, open_client_sockets, [])
        for current_socket in rlist:
            if current_socket is server_socket:
                (new_socket, address) = server_socket.accept()
                open_client_sockets.append(new_socket)
            else:
                data = str(current_socket.recv(1024))
                if data == 'r':
                    open_client_sockets.remove(current_socket)
                    print "Connection with client closed."
                else:
                    messages_to_send.append((current_socket, data))
        send_waiting_messages(wlist)


def main():
    server_cycle()
    for client_socket in open_client_sockets:
        client_socket.close()
    server_socket.close()


if __name__ == '__main__':
    main()
