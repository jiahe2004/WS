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
        self.server.listen(self.mod)
        self.mod = mod
        self.switch1 = True
    def server_mod(self):
        self.login_c = False
        self.deck_c = False
        self.close_c = False
        self.who , self.addr = self.server.accept()
        self.server_c()
    def server_c(self):
        while not self.close_c:
            try:
                ""
            except:
                
                """
        while True:
            indata = who.recv(1024)
            if len(indata) == 0 or indata.decode() == "strict":
                who.close()
                break
            if indata.decode() != "WS by try login" or not login_c:
                who.send("error".encode())
                break
            else:
                login_c = True


                print('recv: '+indata.decode())

                outdata = 'echo '+indata.decode()
                who.send(outdata.encode())
        """
if __name__ == "__main__":
    """"""
                    
            

