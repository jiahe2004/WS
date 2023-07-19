import socket
import threading

HOST = '127.0.0.1'
PART = 8885


def stop():
    """test"""


class server:
    def __init__(self,mod=int) -> None:
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.server.bind((HOST,PART))
        self.mod = mod
        self.switch1 = True
        self.__server = threading.Thread(target=server.server(self))
    def star(self):
        self.server.listen(self.mod)
        print("server star")
        
    def server(self):
        while self.switch1:
            meg , addr = self.server.accept()
            print("call from: "+str(addr))
            while True:
                indata = meg.recv(1024)
                if len(indata) == 0:
                    meg.close()
                    break
                print('recv: '+indata.decode())

                outdata = 'echo '+indata.decode()
                meg.send(outdata.encode())
if __name__ == "__main__":
    server(1).star()
                    
            

