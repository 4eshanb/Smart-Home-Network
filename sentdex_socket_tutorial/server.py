import socket
import time
import pickle #for serialization aka turning objects/data structures into bytes

HEADERSIZE = 10

#https://www.youtube.com/watch?v=Lbfe3-v7yE0
#https://www.youtube.com/watch?v=8A4dqoGL62E
#https://www.youtube.com/watch?v=WM1z8soch0Q

# AF = address family
# INET = Internet
# AF_INET = ipv4
# AF_INET refers to addresses from the internet, IP addresses specifically. 
# AF_INET is an address family that is used to designate the type of addresses 
# that your socket can communicate with (in this case, Internet Protocol v4 addresses). 
# When you create a socket, you have to specify its address family, and then you can only 
# use addresses of that type with the socket. 
# For the most part, sticking with AF_INETfor socket programming over a network is the safest option. 

# SOCK_STREAM = tcp

# a socket is an endpoint that recieves/sends data
# the server is the receiver
# the socket sits on an IP address on a port.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a tuple. The tuple will be an ip address and a port
# use 4-digit port becuase lower numbers are used for other programs
s.bind((socket.gethostname(), 1234))

# server listens for data. The server has a queue of 5 is there is a lot of traffic
s.listen(5)

# listen forever for connections
while True:
    # if anyone tries to connect,we allow it
    # Store the client socket object into the variable clientsocket
    # store the client's address into address.

    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")


    # might want a header, whisch lets program know how big is the message and other information
    # maybe have a fixed length header, so that no one can mess with the header, as opposed to something simple like "begin"

    #msg = "Welcome to server!"
    d = {1: "Hey", 2: "There"}
    msg = pickle.dumps(d)

    # length of message, < means left aligned, then the headersize. 
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg

    # send info to client socket.
    # our local version of client socket
    #clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    clientsocket.send(msg)

