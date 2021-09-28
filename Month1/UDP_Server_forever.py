from socket import *
#udp先启动那一端都可以
ip_sort=('127.0.0.1',8000)
buffer_size=1024

# 创建socket链接 SOCK_DGRAM->udp协议
udp_server=socket(AF_INET,SOCK_DGRAM)
# 绑定ip和端口
udp_server.bind(ip_sort)

while True:
	data,addr=udp_server.recvfrom(buffer_size)#tcp是recv，udp是recvfrom
	print(data.decode('utf-8'))
	msg=input('>>: ')
	udp_server.sendto(msg.encode('utf-8'),addr)#tcp是send，udp是sendto

udp_server.close()