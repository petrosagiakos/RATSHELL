class clentry:
    def __init__(self,cl,os,name,user):
        self.fd=cl[0]
        self.addr=cl[1]
        self.os=os
        self.name=name
        self.user=user
        self.client_id=0
    def entry_print(self):
        print(self.client_id," ",self.addr[0]," ",self.os," ",self.name," ",self.user)