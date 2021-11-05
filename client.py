import time
import socket



def broadcastRelay(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('0.0.0.0',port))
    print("Listening for broadcasts on port: "+str(port))
    while True:
        addr,port=s.recvfrom(4096)[1]
        print("broadcast from "+str(addr)+" "+str(port))
        s.sendto(str.encode('this is testing'),(str(addr),port))

broadcastRelay(12348)
