import platform
import socket
from exec import tools

PORT=555
HOST="127.0.0.1"

class Client:
    def __init__(self):
        self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connect()
        
        self.osm=platform.system()
    
    def connect(self):
        self.s.connect((HOST,PORT))

    def exec(self,size):
        print(self.osm)
        while True:
            cmd1=self.s.recv(size).decode()
            if cmd1=="ls":
                self.s.send(tools.ls(self.osm,self.s).encode())
            elif cmd1=="pwd":
                self.s.send(tools.pwd(self.osm,self.s).encode())
            elif cmd1=="exit":
                print("exit")
                
                self.s.close()
                break
        

client = Client()
client.exec(1024)





