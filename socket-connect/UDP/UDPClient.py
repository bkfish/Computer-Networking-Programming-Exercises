import socket
serverName= 'localhost'
serverPort= 9999
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#AF_INET 使用IPV4 SOCK_DGRAM意味着UDP
message=input('输入小写字母： ')
s.sendto(message.encode(),(serverName,serverPort))
modifiedMessage,serverAddress=s.recvfrom(1024)

print("Receive from %s:%s"% serverAddress,end=" ")

print("Content: "+modifiedMessage.decode())#1024是缓存长度
s.close()