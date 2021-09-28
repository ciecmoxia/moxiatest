'''
TCP粘包，两种情况：客户端发的信息短且快，服务端一遍就全接受了；服务端的buffer_size设置的小，超出来的就舍弃了
tcp的recv()和send()是对应关系，但不是一一对应，分别在各自的缓冲区进行操作
'''
import socket# 客户端：
import time

# a. 买手机 tcp_client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# b. 拨号 tcp_client.connect(("服务端 ip", 服务端端口))
tcp_client.connect(('127.0.0.1',8000))

# c. 发消息，说话 tcp_client.send(发送的是字节数据需要编码)
tcp_client.send('hello，我是客户端'.encode('utf-8'))
time.sleep(2)
tcp_client.send('hello，我是客户端'.encode('utf-8'))
time.sleep(2)
tcp_client.send('hello，我是客户端'.encode('utf-8'))
time.sleep(2)

# d. 接收消息，听话 data = tcp_client.recv(1024)
data=tcp_client.recv(1024)
print('服务端说:',data.decode('utf-8'))
# e. 挂电话 tcp_client.close()
tcp_client.close()