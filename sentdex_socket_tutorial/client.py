import socket
import pickle

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# instead of binding, we connect to a tuple
# client will be remote to server usually. They are usually not on the same machine. This case is diff.

s.connect((socket.gethostname(), 1234))

# recive message from server
# we receive 1024 bytes at most of data. It's a buffer

while True:
    # now we are using a buffer of 8. And we loop infinitely to receive all the data
    full_msg = b""
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        print(f"full message length: {msglen}")
        full_msg += msg
        print(len(full_msg))

        if len(full_msg) - HEADERSIZE == msglen:
            print("full message recieved")
            print(full_msg[HEADERSIZE:])

            d = pickle.loads(full_msg[HEADERSIZE:])
            print(d)
            
            new_msg = True
            full_msg = b""

        #if len(msg) <= 0:
        #   break

print(full_msg)
