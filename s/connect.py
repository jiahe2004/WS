import socket
class connect_server:
    def __init__(self) -> None:
        self.connet = socket.socket(socket.AF_INET,socket.SOCK_STREAM)