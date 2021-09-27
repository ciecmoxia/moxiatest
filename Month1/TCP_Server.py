# 网络的概念，五层：应用层（应用）、传输层（tcp、udp端口）、网络层（ip）、数据链路层（ethernet mac地址）、物理层（0和1）
'''
Socket编程（抽象层、套接字），Socket 是应用层与 TCP/IP 协议族通信的中间软件抽象层，它是一组接口。
在设计模式中，Socket 其实就是一个门面模式，它把复杂的TCP/IP 协议族隐藏在 Socket 接口后面，对用户来说，
一组简单的接口就是全部，让 Socket去组织数据，以符合指定的协议。所以，我们无需深入理解 tcp/udp 协议，
socket 已经为我们封装好了，我们只需要遵循socket 的规定去编程，写出的程序自然就是遵循 tcp/udp 标准的。
也有人将 socket 说成 ip+port，ip 是用来标识互联网中的一台主机的位置，而 port 是用来标识这台机器上的
一个应用程序，ip 地址是配置到网卡上的，而 port 是应用程序开启的，ip 与 port 的绑定就标识了互联网中
独一无二的一个应用程序。而程序的 pid 是同一台机器上不同进程或者线程的标识
unix 一切皆文件，基于文件的套接字调用的就是底层的文件系统来取数据，两个套接字进
程运行在同一机器，可以通过访问同一个文件系统间接完成通信

'''
# tcp 的整个流程类似打电话的一个过程：
import socket # 服务端：

# a. 建立链接，买手机 tcp_server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 基于文件类型的套接字家族,名字：AF_UNIX,基于网络类型的套接字家族,名字：AF_INET ; SOCK_STREAM：TCP协议,Sock_DGRAM：UDP协议
tcp_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# b. 绑定电话卡 tcp_server.bind(("ip", 端口))
tcp_server.bind(('127.0.0.1',8000))
# c. 待机 tcp_server.listen(最大链接数)
tcp_server.listen(5)
# d. 接听电话 conn, addr = tcp_server.accept()得到链接和对方地址
conn,addr=tcp_server.accept()
# e. 接收消息，听话 data = conn.recv(接收字节数)
data=conn.recv(1024)
print('客户端说：',data.decode('utf-8'))# .encode('utf-8')改为.decode('utf-8')
# f. 发消息，说话 conn.send(发送的是字节数据需要编码)
conn.send('我是服务端！'.encode('utf-8'))
# g. 挂电话 conn.close()
conn.close()
# h. 关闭服务端手机关机 tcp_server.close()
tcp_server.close()
