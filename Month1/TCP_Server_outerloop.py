# 网络的概念，五层：应用层（应用）、传输层（tcp、udp端口）、网络层（ip）、数据链路层（ethernet mac地址）、物理层（0和1）

# tcp 的整个流程类似打电话的一个过程：
import socket # 服务端：
# a. 建立链接，买手机 tcp_server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 基于文件类型的套接字家族,名字：AF_UNIX,基于网络类型的套接字家族,名字：AF_INET ; SOCK_STREAM：TCP协议,Sock_DGRAM：UDP协议
tcp_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# b. 绑定电话卡 tcp_server.bind(("ip", 端口))
tcp_server.bind(('127.0.0.1',8000))
# c. 待机 tcp_server.listen(最大链接数)
back_log=5
buffer_size=1024
tcp_server.listen(back_log)

while True:	# 链接循环，外层循环，保证服务端永久执行
	# d. 接听电话
	print('很高兴为大家服务！')
	conn,addr=tcp_server.accept()# 三次握手 没有数据，只是连接，合并了两次握手
	#在此之前阻塞，等待信息

	while True:	# 通信循环，内层循环
		try:
			# e. 接收消息
			data=conn.recv(buffer_size)
			if not data: break
			# 客户端强制中断，linux会一直返回空给服务端，用if not data: break解决
			# 客户端强制中断，windows会抛异常给服务端，用try\except解决

			if data.decode('utf-8')=='exit':
				conn.send(data)
				break

			print('客户端说：',data.decode('utf-8'))# .encode('utf-8')改为.decode('utf-8')
			# f. 发消息
			msg=input('>>: ').strip()
			if not msg: continue
			conn.send(msg.encode('utf-8'))
		except Exception as e:
			print('出现异常，异常信息为：',e)
			break

	# g. 挂电话,循环里接电话，一一对应
	conn.close()# 四次挥手 考虑到有数据是否传完
# h. 关闭服务端手机关机
tcp_server.close()
