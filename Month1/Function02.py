# 自定义函数 有参 有返回值
# return 1、跳出方法 2、返回值 可以是多个
# 编写一个函数获取绝对值
def sxt_abs(num):
	if num >= 0:
		return num
	else:
		return -num
def sxt_abs2(num):
	if num >= 0:
		return num
	return -num
def sxt_abs3(num):
	return num if num >= 0 else -num

# 多个返回值
def sxt_abs4(num):
	if num >= 0:
		return num, "正数"#多个返回元组
	return -num, '负数'
print(sxt_abs(-5), sxt_abs2(-5), sxt_abs3(-5))
box = sxt_abs4(-5)
print(box)#(5, '负数')

import random
# 自定义函数
# 确保后期所有的状态的值类型保持一致
def check_month(month):
# 非正常情况
	if not 1 <= month <= 12:
		return # None
	else:
		m = month
		m //= 3 # 判断
		if m == 1:
			return '春困'
		elif m == 2:
			return 1
		elif m == 3:
			return -1
		else:
			return '冬眠'
box = check_month(random.randint(1,12))
print(box)
box = check_month(random.randint(1,12))
print(box)
box = check_month(random.randint(1,12))
print(box)

# __name__ -> 自身使用返回：__main__，别人使用返回：模块名(my_def__name__)
print(__name__) # 构造函数 -> 模拟 abs()
def sxt_abs(num):
	'''__doc__注释打印'''
	if num >= 0:
		return num
	else:
		return -num
print(sxt_abs.__doc__)
# 使用函数
if __name__ == '__main__':
	box = sxt_abs(-5)
	print(box) # 构造函数 -> 模拟 range()

def sxt_range(min, max):
	_list = []
	while min < max:
		_list.append(min)
		min += 1
	return _list
if __name__ == '__main__':
	print(sxt_range(0,5))
# 使用函数
if __name__ == '__main__':
	for i in sxt_range(0,5):
		print(i)

def fun1(a,b,c):
	print("a={},b={},c={}".format(a,b,c))
fun1(b=1,c=2,a=3)#位置参数
# fun1(a=1,v=2,d=3)错误
# 默认参数必须在形参末尾
def fun2(a,c,b=3):
	print("a={},b={},c={}".format(a,b,c))
#强制关键字参数,*之后必须按名称复制
def fun3(a,*,b):
	print(a,b)
fun3(1,b=3)#1 3
#可变参数,*b可以传各种类型,多个，包括列表、元组等,*b打印出来的是元祖
def fun4(a,*b):
	print(a,b)
fun4(1,'sad',[2,3],(1,3))
#可变强制关键字，**b
def fun5(a,**b):
	print(a,b)
fun5(1,n=1,m=2)
fun5(1,**{'n':2,'m':3})#**拆包

#可变参数
def fun6(a,*b,c):
	print(a,b,c)
fun6(1,'sad',[2,3],(1,3),c=5)

def fun7(a,*,b,c='默认'):
	print(a,b,c)
fun7(1,b=2,c=3)

def fun8(a,*b,**c):
	print(a,b,c)
fun8(1,'sad',[2,3],(1,3),c=5)
fun8(1,'sad',[2,3],(1,3),**{'c':4})

def dog(name,shape='big',action='叫',color='yellow'):
	print("狗名：",name,end=" ")
	print("大小：",shape,end=" ")
	print("动作：", action, end=" ")
	print("颜色：", color, end="\n")
#正确传参
dog("阿黄")
dog(name="阿黄")
dog(name="阿黄",action="吃")
dog(color="黄",name="yellow")
dog("阿黄","small","run")
dog("阿黄",color="white")
#错误传参
# dog("阿黄",name="yellow")
# dog("阿黄",ab="c")

#python解释性语言，没有编译过程
def cat(*arge,sep="/"):
	print(sep.join(arge))
cat("asd","asd","sdf")
cat("asd","asd","sdf",sep="-")

#全局变量global
a='a'
def fun9():
	global a#先声明后赋值，不然报错
	a='b'#就近原则
	print(a)
	a="c"
fun9()
print(a)

def out_fun():
	o="out"
	def in_fun():
		o="in"
		print(o)
	print(o,"!!")
	return in_fun()#in_fun()或print(o)不要用
out_fun()
# out_fun().in_fun()python不能这么用