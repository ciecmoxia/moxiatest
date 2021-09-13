'''
Input Stream 、 Output Stream 输入流、输出流
转化为二进制读取，写入 不需要考虑字符集
类比于搬家：
打开门 								-> open()
搬家(一次一次搬，一卡车一卡车搬，一次性搬) -> read() read(大小)+循环
整理 								-> 分析、处理
关门 								-> close()

#open
open(file, mode='r', buffering=-1, encoding=None, errors=None,
newline=None, closefd=True)
file：文件路径
mode：操作方式 r读 w写 a写 rb读取二进制 wb写入二进制 ab写入二进制
buffering：读取的大小
encoding：指定字符集
errors：错误解决策略
newline：只对纯文有效，区分换行符
closefd：是否为文件

#close
使用完流以后，务必要关闭，先打开的后关闭

#序列化和反序列化
字符转字节，字节转字符

#文本与文件
纯文本：字符集，逐行读取
文件：pdf、word、电影、图片、音乐，不支持逐行读取，不需要考虑字符集，考虑字节

1. r -> 读取
2. rb -> 读取二进制
3. w -> 文件不存在，创建文件再写入；文件存在，清空文件内容再写入
4. a -> 第一次，文件不存在，创建文件再写入；多次，文件存在，追加内容
5. wb -> 写入二进制
6. ab -> 追加二进制
open(r"文件路径", "读或写", encoding=编码字符集)
'''
'''
#一次性读取
src=open(r'F:\软考必备\python学习资料\Python初级day10~11函数、IO、字符串\day11-IO\代码\io\first.txt','r',encoding='GBK')#r''保留路径中的原样格式
print(type(src))
data=src.read()
print(data)
src.close()

#多次循环读取
src=open(r'F:\软考必备\python学习资料\Python初级day10~11函数、IO、字符串\day11-IO\代码\io\first.txt','r',encoding='GBK')#r''保留路径中的原样格式
print(type(src))
# data=src.read()
# for i in data:
# 	print(i.rstrip(),end="")

my_data=[]
size=2
while True:
	data=src.read(size)
	# print(type(data))
	if not data:
		break
	my_data.append(data)
print(my_data)
print(','.join(my_data))
src.close()

#按行读取
src=open(r'F:\软考必备\python学习资料\Python初级day10~11函数、IO、字符串\day11-IO\代码\io\first.txt','r',encoding='GBK')#r''保留路径中的原样格式
print(type(src))
# data=src.readline()#里面的参数只是设置读一行的前几个
# print(data)
# data=src.readline()
# for i in data:
# 	print(i,end="")

my_data=[]
while True:
	data=src.readline()
	# print(type(data))
	if not data:
		break
	my_data.append(data)
print(my_data)
print(','.join(my_data))
src.close()

src=open(r'F:\软考必备\python学习资料\Python初级day10~11函数、IO、字符串\day11-IO\代码\io\first.txt','r',encoding='GBK')#r''保留路径中的原样格式
print(type(src))
data=src.readlines()#返回的是一个列表list
print(type(data))
print(data)
for i in data:
	print(i,end="")
src.close()

#读取二进制
src=open(r'F:\软考必备\python学习资料\Python初级day10~11函数、IO、字符串\day11-IO\代码\io\first.txt','rb')#r''保留路径中的原样格式
print(type(src))
data=src.read()
print(type(data))
print(len(data))
print(data)
print(data.decode('GBK'),end="")#GBK三个字节，errors="ignore"
src.close()


#写出文件，w文件不存在则创建，再写入；存在则清空，再写入。 a文件不存在创建，再写入，存在追加，不会清空
f=open(r'F:\软考必备\python学习资料\Python初级day10~11函数、IO、字符串\day11-IO\代码\io\second.txt','a',encoding='utf-8')#r''保留路径中的原样格式
data='人生苦短，我学python\n'
len=f.write(data)
print(len)
f.close()
#读取二进制
# f=open(r'F:\软考必备\python学习资料\Python初级day10~11函数、IO、字符串\day11-IO\代码\io\second.txt','wb')#r''保留路径中的原样格式
# data='人生苦短，我学python\n'.encode('utf-8')


#拷贝文件，边读边写
def copy(src_path,end_path):
	src=open(src_path,'rb')
	end=open(end_path,'wb')

	while True:
		data=src.read(1024)
		if not data:
			break
		end.write(data)
	# data=src.read()
	# end.write(data)

	end.close()
	src.close()

copy(r'F:\软考必备\python学习资料\Python初级day10~11函数、IO、字符串\day11-IO\代码\io\first.txt',
	 r'F:\软考必备\python学习资料\Python初级day10~11函数、IO、字符串\day11-IO\代码\io\first1.txt')
'''
#with关键字,可以帮你关close
def copy(src_path,end_path):
	with open(src_path,'rb') as src:
		with open(end_path,'wb') as end:
	#	with open(src_path,'rb') as src,open(end_path,'wb') as end:
			while True:
				data=src.read(1024)
				if not data:
					break
				end.write(data)
			# data=src.read()
			# end.write(data)

copy(r'F:\软考必备\python学习资料\Python初级day10~11函数、IO、字符串\day11-IO\代码\io\first.txt',
	 r'F:\软考必备\python学习资料\Python初级day10~11函数、IO、字符串\day11-IO\代码\io\first1.txt')