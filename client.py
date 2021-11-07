import socket
import netifaces as ni

def getBroadcastIP():
    ips=[]
    #ip  = socket.gethostbyname_ex(socket.gethostname())[2][0]  # Obtain your IP address
    #net = ipaddress.IPv4Network(ip + '/' + netmask, False)
    #broadcast = str(net.broadcast_address)
    ifaces = ni.interfaces()
    for iface in ifaces:
        try:
            print(ni.ifaddresses(iface)[ni.AF_INET])
            ips.append(ni.ifaddresses(iface)[ni.AF_INET][0]["broadcast"])
        except:
            pass
    return ips

def broadcast(port):
    timeout=3
    retry=21
    server=""
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.bind(('0.0.0.0', 0))
    s.settimeout(timeout)
    for x in range(retry):
        try:
            for broad in getBroadcastIP():
                s.sendto(str.encode('test'),(broad,port))
            data,address=s.recvfrom(4096)
            return address[0]
        except socket.timeout:
            print("timeout")
    
print("server is at "+str(broadcast(12349)))
