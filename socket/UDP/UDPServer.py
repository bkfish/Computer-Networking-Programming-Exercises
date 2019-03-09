import socket
serverName= 'localhost'
serverPort= 9999
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((serverName,serverPort))
print("开始监听9999端口")
while True:
	data,addr=s.recvfrom(1024)
	data_decode=data.decode()
	print("Receive from %s:%s"% addr)
	newMessage=data_decode.upper()
	s.sendto(newMessage.encode(),addr)