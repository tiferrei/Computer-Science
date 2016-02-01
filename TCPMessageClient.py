# TCPMessageClient.py

import socket
import select
import string
import time
import sys

def prompt():
    sys.stdout.write('Message -> ')
    sys.stdout.flush()

#main function
if __name__ == "__main__":

    if(len(sys.argv) < 3) :
        print('Usage : python3 TCPMessageClient.py hostname port')
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print('Connection failed. Please check your values and run the script again.')
        sys.exit()

    print('Connection to server established successfully.')
    prompt()

    while 1:
        socket_list = [sys.stdin, s]

        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])

        for sock in read_sockets:
            #incoming message from remote server
            if sock == s:
                data = sock.recv(1024)
                data = data.decode('UTF-8')
                if not data :
                    print('\nDisconnected from the server.')
                    sys.exit()
                else :
                    #print data
                    sys.stdout.write(data)
                    prompt()

            #user entered a message
            else :
                msg = sys.stdin.readline()
                msg = msg.encode()
                s.send(msg)
                prompt()
