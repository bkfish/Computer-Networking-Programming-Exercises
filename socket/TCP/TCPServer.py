from socket import *
dest_ip = 'localhost'
dest_port = 9999
tcpSerSocket = socket(AF_INET, SOCK_STREAM)  
tcpSerSocket.bind((dest_ip,dest_port))
tcpSerSocket.listen(128)
print("等待连接!")
newSocket, clientAddr = tcpSerSocket.accept()
recvData = newSocket.recv(1024)
print('接收到的数据为：', recvData.decode('gbk'))
InputMessage=input("请输入回复内容： ")
newSocket.send(InputMessage.encode("gbk"))
newSocket.close()
tcpSerSocket.close()