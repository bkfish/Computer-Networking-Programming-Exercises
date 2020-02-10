#-*- coding: utf-8 -*-
import os,sys
from socket import *
class TcpClient:
    HOST='127.0.0.1'
    PORT=1122
    BUFSIZ=2048
    ADDR=(HOST, PORT)
    def __init__(self):
        self.client=socket(AF_INET, SOCK_STREAM)
        self.client.connect(self.ADDR)
        self.client.settimeout(3)
        while True:
            self.client.send("whoami".encode('utf8'))
            pwd_addr=self.client.recv(self.BUFSIZ)
            print("Hostname:"+str(self.HOST)+" Port:"+str(self.PORT)+" "+pwd_addr.decode('utf8')[0:-1],end=">")
            data=input()
            if not data:
                break
            self.client.send(data.encode('utf8'))
            print('Execute %s：%s' %(self.HOST,data))
            if data.upper()=="QUIT":
                break
            try:
                data=self.client.recv(self.BUFSIZ)
            except Exception as e:
                print("Mabey No response Or error")
                continue
            
                
            print('Receive：%s' %(data.decode('utf8')))
if __name__ == '__main__':
    client=TcpClient()