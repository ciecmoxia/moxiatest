import os  # OS模块

# https://www.runoob.com/python/os-file-methods.html
# 操作文件工具模块
# 字节 bytes 转化 kb\m\g
'''
def get_k_m_b(bytes_len):
	try:
		len = float(bytes_len)
		kb = len/ 1024
	except:
		print("传入的字节数不对")
		return "Error"

	if kb >= 1024:
		M = kb / 1024
		if M >= 1024:
			G = M / 1024
			return "%fG" % (G)
		else:
			return "%fM" % (M)
	else:
		return "%fkb" % (kb) # 获取文件大小

# 获取文件大小
def getFileSize(path):
	try:
		size = os.path.getsize(path)
		return get_k_m_b(size)
	except Exception as ex:
		print(ex) # 获取文件夹大小

def getDirSize(path):
	total_size = 0
	try:
		parents = os.walk(path)
		for root, dirs, files in parents:
			for sub in files:
				size = os.path.getsize(path + sub)
				total_size += size
		return get_k_m_b(total_size)
	except Exception as ex:
		print(ex)

def main():
	print(getDirSize(r"XXXXX.py"))
	print(getFileSize(r"xxxxxx.py"))#\\文件夹、\\xx.py文件
	print(get_k_m_b(536870912))
if "__main__" == __name__:
	main()


import shutil
# 复制文件
# shutil.copyfile(src, dest)
# 复制文件到文件或者目录，会改变元信息
# shutil.copy(src, dest)
# 复制文件到文件或者目录,不会改变元信息
shutil.copy2("haha.txt", "haha2.txt") # 拷贝目录
# shutil.copytree(src, dst)
# 拷贝的是文件对象
src = open(r"D:\Dylan\myPython\day08-IO\code\first.txt", 'r', encoding="GBK")
dest = open(r"D:\Dylan\myPython\day08-IO\code\other\first_copy.txt", 'w',
encoding="GBK")
shutil.copyfileobj(src, dest)
src.close()
dest.close()
# 移动文件
# shutil.move('haha.txt', 'file')
# 删除文件目录以及子文件目录
# shutil.rmtree("file")
# 压缩
# shutil.make_archive('good', 'zip',r'D:\Dylan\myPython\day08-IO\code\other\zip\\')
# 解压
# shutil.unpack_archive(r'D:\Dylan\myPython\day08-IO\code\other\zip\good.zip')


# 对象的序列化和反序列化
import pickle
# 序列化到内存二进制
p = {'first':'程','second':'许愿'}
data = pickle.dumps(p)
print(data)
# 反序列化
p = pickle.loads(data)
print(p)
# 序列化到文件
p = {'first':'程','second':'许愿'}
with open('obj.txt', 'wb') as f:
	pickle.dump(p,f)
# 反序列化
with open('obj.txt', 'rb') as f:
	p = pickle.load(f)

print(p['first'])

# https://www.runoob.com/python/python-json.html
# 对象的序列化和反序列化
import json
# 转 json 序列化
p = {'first':'程','second':'许愿'}
msg = json.dumps(p)
print(type(msg))
# json 反序列化
p = json.loads(msg)
print(p,type(p))
# 转 json 序列化
msg = json.dumps({'a': 'hello', 'b': 7}, sort_keys=True, indent=4,
separators=(',', ': '))
print(msg) # 显示格式
# json 反序列化
p = json.loads(msg)
print(p) # 转 json 序列化
p = {'first':'程','second':'许愿'}
with open('json.txt','w') as f:
	json.dump(p,f)
# json 反序列化
with open('json.txt','r') as f:
	p = json.load(f)
	print(p)
'''
