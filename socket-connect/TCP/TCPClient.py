from socket import *
dest_ip = 'localhost'
dest_port = 9999
tcp_socket_client = socket(AF_INET,SOCK_STREAM)
#AF_INET 使用IPV4 SOCK_STREAM意味着TCP
tcp_socket_client.connect((dest_ip,dest_port))
data_info = input('请输入内容')
tcp_socket_client.send(data_info.encode('gbk'))
data_re = tcp_socket_client.recv(1024)
print(data_re.decode('gbk'))
tcp_socket_client.close()