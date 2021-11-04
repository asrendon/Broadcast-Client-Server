import time
import socket
import ipaddress
import netifaces as ni

def getBroadcastIP():
    ips=[]
    ifaces = ni.interfaces()
    for iface in ifaces:
        try:
            ips.append(ni.ifaddresses(iface)[ni.AF_INET][0]['broadcast'])
        except:
            pass
    return ips

def broadcastRelay(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((getBroadcastIP()[0],port))
    print("Listening for broadcasts on port: "+str(port))
    while True:
        addr,port=s.recvfrom(4096)[1]
        print("broadcast from "+str(addr)+" "+str(port))
        s.sendto(str.encode('this is testing'),(str(addr),port))

broadcastRelay(12348)