from socket import *
import time
ip_sort=('127.0.0.1',8000)
buffer_size=1024
udp_client=socket(AF_INET,SOCK_DGRAM)

while True:
	msg=input('>>: ')
	udp_client.sendto(msg.encode('utf-8'),ip_sort)
	data,addr=udp_client.recvfrom(buffer_size)
	print(data.decode('utf-8'))

udp_client.close()