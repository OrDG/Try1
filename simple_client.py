import socket
import select
import msvcrt

PORT = 1025
HOME = '127.0.0.1'


my_socket = socket.socket()
my_socket.connect((HOME, PORT))
inout = [my_socket]


def main():
    while True:
        rlist, wlist, xlist = select.select(inout, inout, [])
        if len(wlist) != 0:
            if msvcrt.kbhit():
                command = msvcrt.getch()
                print command
                my_socket.send(command)
                if command == 'r':
                    break
        if len(rlist) != 0:
            data = my_socket.recv(1024)
            print data

    my_socket.close()


if __name__ == '__main__':
    main()
