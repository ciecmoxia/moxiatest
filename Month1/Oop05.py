# 多态，Python 严格意义上讲，是没有多态的，面试的时候千万别说 Python 有多态
# 抽象：我去买水果 我去买苹果
# 鸭子模型 -> 鸭子两条腿走路，其他是两条腿走路的我们都可以看作是鸭子
'''
多态有些弄不明白
class Bird(object):
	def fly(self):
		print("鸟会飞。。。")
class Pigeon(Bird):
	def fly(self):
		print("鸽子在飞。。。")
class Parrot(Bird):
	def fly(self):
		print("鹦鹉在飞。。。")
class Person(object):
	def fly(self):
		print("鸟人在飞。。。")
def fly(bird):
	bird.fly()
pigeon = Pigeon()
parrot = Parrot()
person = Person()
fly(pigeon)
fly(parrot)
fly(person) # 鸭子模型
'''
import random
# 练习；构建车库，买车，提车，人开车
'''
1. 确定类 Car Carport Person -> 需要初始化 绑定属性
2. 买车
3. 提车
4. 开车

# 车 -> 开辟空间 初始化 返回引用
class Car(object):
	def __init__(self, color, name):
		self.color = color
		self.name = name
	def running(self):
		return "{s.color}的{s.name}车在狂奔！".format(s = self)

# 宝马车继承车类
class Bmw(Car):
	def __init__(self, color):
		self.color = color
		self.name = "宝马" # 奔驰车继承车类

class Benz(Car):
	def __init__(self, color):
		super(Benz, self).__init__(color, "奔驰")

# QQ 车继承车类
class QQ(Car):
	def __init__(self, color):
		super().__init__(color, "奇瑞 QQ")
	def running(self):
		return "{s.color}颜色的{s.name}车在狂奔，光脚的不怕穿鞋的！".format(s=self)

# 车库
class Carport(object):
	# 初始化对象信息
	def __init__(self):
		self.cars = []
	# 买车
	def buy_car(self, car):
		self.cars.append(car)
	# 提车
	def get_car(self):
		return self.cars[random.randint(0, len(self.cars) - 1)]
	# 人
class Person(object):
	# 开车
	def drive(self, car):
		return car.running()

class Cpu:
	def running(self):
		return 'Cpu在狂奔...'

def main():
	# 构建车库
	car_port = Carport()
	# 买车
	benz = Benz('白色')
	bmw = Bmw('黑色')
	qq = QQ('黄色')
	car_port.buy_car(benz)
	car_port.buy_car(bmw)
	car_port.buy_car(qq)
	# 提车
	result_car = car_port.get_car()
	# 人开车
	p = Person()
	print(p.drive(result_car))
	#鸭子模型
	c=Cpu()
	print(p.drive(c))
if '__main__' == __name__:
	main()
'''
'''
	多继承
	a. 多个类继承时，子类在前，父类在后
	b. 位置会影响结果
	查看多继承的继承顺序：类.__mro__或类.mro()
class A:
	pass
class B(A):
	pass
class C(A):
	pass
class D:
	pass
class E(C):
	pass
class G(D):
	pass
class F(E, G, B):
	pass
if __name__ == '__main__':
	print(F.__mro__)

class Jinyong(object):
	def xie_wuxia(self):
		print('会写武侠小说')

class Hongqg(Jinyong,object):
	def hui_gongfu(self):
		print('会降龙十八掌')

class Gujing(Hongqg,Jinyong,object):#从左到右严格依次继承，父类等级不同，从小到大
	pass

def main():
	gj=Gujing()
	print(Gujing.__mro__)#继承链
	gj.xie_wuxia()
	gj.hui_gongfu()

if '__main__'==__name__:
	main()
'''
'''
为了可以让程序正常的执行，所以要处理异常
内因：程序不够健壮，日积月累提高代码健壮性
外因：做好防护工作
BaseException：所有异常类的基类
Exception：常规异常的基类
NameError TypeError ValueError ZeroDivisionError
格式：
#处理异常：主动处理
try:
	可能会异常的代码块
except(异常|多个异常) as e:
	解决异常的代码块
else:
	没有异常会执行的代码块
finally:
	有没有异常都会执行，先于 return 执行

def testExcept():
	try:
		#age = input('请输入你的年龄') # TypeError
		#age += 2 # TypeError
		a = int('2') # ValueError
		return
	except(TypeError, ValueError) as e:
		if isinstance(e, TypeError):
			print("输入的数字格式不合法，请输入纯数字", e)
		elif isinstance(e, ValueError):
			print("数据类型转换失败，请输入纯数字的字符串", e)
			return
	else:
		print("程序写的很完美，没有异常")
	finally:
		print("有没有异常都会执行，先于 return 执行")
testExcept()

# 异常处理：抛出异常
# 谁调用谁处理
def testExcept():
	print("程序正常执行")
	raise PermissionError("你懂得...")
def test():
	try:
		testExcept()
	except Exception as e:
		print("处理异常的代码块")
		raise PermissionError("继续出错了...")
	finally:
		print("不管有没有异常我都执行")
test()

# 异常处理：通过健壮性
# 判断一个人的年龄，如果大于 18 岁提醒戒烟，小于 18 告诉他未成年不允许吸烟
def testExcept(str_age):
	# 判断是否是整数
	flag = (type(1) == type(str_age)) # False 说明是字符串
	# 判断是否为整数字符串
	if not flag:
		flag = (type('a') == type(str_age)) and str_age.isdigit() #isdigit()作用是判断字符串是否为整数
	# 判断是否成年
	if flag:
		age = int(str_age)
		if age > 18:
			print("吸烟有害健康，尽早戒烟有益健康")
		else:
			print("未成年不允许吸烟")
	else:
		print("非法格式")
testExcept('20aa')
'''

#模拟用户注册、异常处理、自定义异常
'''
	1、用户输入注册信息
	2、判断是否为纯数字
	3、判断长度
	4、注册成功
'''
class CustomException(Exception):
	#初始化信息
	def __init__(self,*args,**kwargs):
		super(CustomException, self).__init__(*args,**kwargs)

def username():#注册
	# 1、用户输入注册信息
	while True:
		str_name=input('请输入注册用户名： ')
		# if len(str_name)==0:
		# 	raise CustomException('用户名不能为空！')
		# print(len(str_name))
		# 3、判断长度,如果表达式成立抛出异常
		# if 6>len(str_name) or len(str_name)>11:
		# 	raise CustomException('用户名不合法请输入6—11长度的用户名')
		# elif str_name.islower()is False:
		# 	raise CustomException('请输入字母')
		if 6<len(str_name) and len(str_name)<11 and str_name.islower()is True:
			return str_name
		elif len(str_name)==0:
			raise CustomException('用户名不能为空！')
		else:
			raise CustomException('用户名不合法，请输入6—11长度的用户名且为字母')
def password(str_name):
	str_pwd = input('请输入用户密码： ')
	if len(str_pwd)==0:
		raise CustomException('密码不能为空！')
	flag=isinstance(str_pwd,str)
	if flag:
		if str_pwd[0].isupper() is False or str_pwd[1].islower()is False or str_pwd[2:].isdigit()is False:
			raise CustomException('密码不合法，必须是1个大写字母+1个小写字母+数字')
		elif len(str_pwd)<6 or len(str_pwd)>12:
			raise CustomException('密码不合法，必须是6—12位')
	# 4、注册成功
	print('恭喜 %s 注册成功！'%str_name)
#ctrl+alt+t
try:
	u=username()
	password(u)
except CustomException as e:
	print('程序异常，异常为：',e)