
import socket
from shprotocol import SHProtocol
#from shclient import SHClient
import shclient

if __name__ == '__main__':
    # create the socket
    # defaults family=AF_INET, type=SOCK_STREAM, proto=0, filno=None
    commsoc = socket.socket()
    commsoc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # connect to localhost:5000
    commsoc.connect(("localhost",50000))
    
    # run the application protocol
    shp = SHProtocol(commsoc)
    shc = shclient.SHClient(shp)
    shc.run()
    
    # close the comm socket
    commsoc.close()