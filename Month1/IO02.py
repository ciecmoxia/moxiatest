#内存
# 导入模块
from io import StringIO
from io import BytesIO
'''
sio=StringIO()
len=sio.write('hello world')
data1=sio.getvalue()
print(data1)

# 1、打开文件
with open(r'F:\软考必备\python学习资料\Python初级day10~11函数、IO、字符串\day11-IO\代码\io\first.txt', 'r') as f , StringIO() as s:
	# 2、读取
	part_size = 2
	while True:
		data = f.read(part_size)
		if data:
		# 3、操作
			#print(data)
			s.write(data)
		else:
			break
	datas = s.getvalue()
	# 4、关闭
s.close()
f.close()
print(datas)

with open(r'F:\软考必备\python学习资料\Python初级day10~11函数、IO、字符串\day11-IO\代码\io\first.txt', 'r') as f , StringIO() as s:
	while True:
		data = s.read(2)
		if data:
			f.write(data)
		else: 
			break
f.close()
s.close()

# 导入模块

with BytesIO() as bio:
	len=bio.write('hello world,hello 中国'.encode('utf_8'))
	data=bio.getvalue()
	print(data.decode('utf_8'))


# 1、打开文件
with open(r'F:\软考必备\python学习资料\Python初级day10~11函数、IO、字符串\day11-IO\代码\io\first.txt', 'rb') as f , BytesIO() as bio:
# 2、读取
	_size = 1024
	while True:
		data = f.read(_size)
		if not data:
			break
		# 3、操作
		# print(data)
		bio.write(data) # 写入内存
	datas = bio.getvalue()
# 4、关闭
bio.close()
f.close()
print(datas)

with open(r'F:\软考必备\python学习资料\Python初级day10~11函数、IO、字符串\day11-IO\代码\io\third.txt', 'wb') as f , BytesIO(datas) as bio:
	while True:
		data = bio.read(1024)
		if not data:
			break
	f.write(data)
f.close()
bio.close()

#seek_tell定向读取,指定游标，返回游标位置
f=open(r'F:\软考必备\python学习资料\Python初级day10~11函数、IO、字符串\day11-IO\代码\io\first.txt', 'r',encoding='GBK')
print(f.seek(0))
data=f.read()
print(f.seek(20))
print(f.tell())
print(data)
'''

