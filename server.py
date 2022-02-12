import time
import socket
import threading

stopFlag=False


def broadcastRelay(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('0.0.0.0',port))
    print("Listening for broadcasts on port: "+str(port))
    while True:
        addr,port=s.recvfrom(4096)[1]
        print("broadcast from "+str(addr)+" "+str(port))
        s.sendto(str.encode('this is testing'),(str(addr),port))

#broadcastRelay(12349)

class RecvThread(threading.Thread):
    def __init__(self,socket):
        threading.Thread.__init__(self)
        self.socket=socket
    def run(self):
        global stopFlag
        while True:
            if stopFlag == True:
                print("RecvThread Ended")
                break
            try:
                addr,port = self.socket.recvfrom(1024)[1]
                self.socket.sendto(str.encode('this is testing'),(str(addr),port))
            except Exception:
                pass






s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(1)
s.bind(('0.0.0.0',12349))
print("Listening on Socket"+ str(s.getsockname()))

recvThread= RecvThread(s)
recvThread.start()
print("server started")

while True:
    try:
        time.sleep(0.5)
    except KeyboardInterrupt:
        print("Exiting...")
        stopFlag = True
        recvThread.join()
        #s.close()
        print("Exited")
        break



