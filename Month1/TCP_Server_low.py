# 网络的概念，五层：应用层（应用）、传输层（tcp、udp端口）、网络层（ip）、数据链路层（ethernet mac地址）、物理层（0和1）

import socket # 服务端：

# a. 建立链接，买手机 tcp_server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 基于文件类型的套接字家族,名字：AF_UNIX,基于网络类型的套接字家族,名字：AF_INET ; SOCK_STREAM：TCP协议,Sock_DGRAM：UDP协议
tcp_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# b. 绑定电话卡 tcp_server.bind(("ip", 端口))
tcp_server.bind(('127.0.0.1',8000))
# c. 待机 tcp_server.listen(最大链接数)
tcp_server.listen(5)
# d. 接听电话 conn, addr = tcp_server.accept()得到链接和对方地址
conn,addr=tcp_server.accept()# 三次握手 没有数据，只是连接，合并了两次握手

# e. 接收消息，听话 data = conn.recv(接收字节数)
data=conn.recv(1024)#出现粘包
print('客户端说：',data.decode('utf-8'))# .encode('utf-8')改为.decode('utf-8')
data=conn.recv(1024)
print('客户端说：',data.decode('utf-8'))# .encode('utf-8')改为.decode('utf-8')
data=conn.recv(1024)
print('客户端说：',data.decode('utf-8'))# .encode('utf-8')改为.decode('utf-8')

# f. 发消息，说话 conn.send(发送的是字节数据需要编码)
conn.send('我是服务端！'.encode('utf-8'))
# g. 挂电话 conn.close()
conn.close()# 四次挥手 考虑到有数据是否传完
# h. 关闭服务端手机关机 tcp_server.close()
tcp_server.close()
