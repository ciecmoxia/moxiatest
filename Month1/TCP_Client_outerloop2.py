import socket# 客户端：
# a. 买手机 tcp_client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# b. 拨号 tcp_client.connect(("服务端 ip", 服务端端口))
tcp_client.connect(('127.0.0.1',8000))
# c. 发消息，说话 tcp_client.send(发送的是字节数据需要编码)
buffer_size=1024

# 开始实现通信循环
while True:
	msg=input('>>: ').strip()
	if not msg: continue

	tcp_client.send(msg.encode('utf-8'))
	# d. 接收消息，听话 data = tcp_client.recv(1024)
	data=tcp_client.recv(buffer_size)
	if data.decode('utf-8')=='exit':
		print('已断开，请重连')
		break
	print('服务端说:',data.decode('utf-8'))

# e. 挂电话 tcp_client.close()
tcp_client.close()