# 属性
# 分类：类属性、实例属性
# 添加,有就修改，没有新加
'''
class User(object):
	height=100
	def __init__(self,name,age):
		self.name=name
		self.age=age
u = User("张三", 18)
u2 = User("李四", 20)
# print(dir(User))
#u.sex = True
#print(u.sex)
setattr(u, "sex", True) # 实例属性 与其他对象无关
setattr(User, "count", 1) # 类属性 所有对象有关
print(u.count)
print(User.count)
#删除
# del u.sex
# del User.count
# print(u.sex)
# print(User.count)
# delattr(u, "sex")
#print(u.sex)
# delattr(User, "age")
# print(User.age)
# 获取
print(u.name)
print(User.height)
print(getattr(u, "name"))
print(getattr(User, "height"))
# 判断 注意__slots__问题
u = User("张三", 18)
u2 = User("李四", 20)
_dict = {'name':'老王'}
print('name' in _dict)
#print('name' in u) # 不可以用 in, in 后面的变量必须可迭代
print('name' in u.__dict__)
print('height' in User.__dict__)
print(hasattr(u, "name"))
print(hasattr(User, "height"))


import json# 属性操作：序列化
# 定义用户类
class User2(object):
	def __init__(self, uname, upwd):
		self.uname = uname
		self.upwd = upwd
	def __str__(self):
		return "{s.uname}的密码为:{s.upwd}".format(s = self)
user = User2("张三", "123")
# 序列化：存储
# print(json.dumps(user)) # 无法直接序列化,TypeError: Object of type User2 is not JSON serializable
# 字典 -> json 格式
def ser(user):
	return user.__dict__
# 序列化
user_dump = json.dumps(user, default = ser, ensure_ascii = False)#ensure_ascii = False不用ASCII码格式，默认用UTF-8格式
print(user_dump)

def hook(_dict):
	return User2(_dict['uname'], _dict['upwd']) # 类似字典获取 -> 返回一个 User2 对象
# 反序列化：获取
user = json.loads(user_dump, object_hook = hook)
print(user)


# 构建用户类
class User2(object):
	# 内置函数的理解
	def __init__(self, name, age):
		self.name = name
		self.age = age
User = User2('张三', 18)
# __doc__
print(User2.__doc__)
# __name__
print(User2.__name__)
print(__name__)
# __module__
print(User2.__module__)
# __bases__
print(User2.__bases__)


class God:
	def show(self):
		print('God')
class People:
	def show(self):
		print('People')
class You(People,God,object):#继承有先后顺序，先自己后父类，但object永远在最后
	# def show(self):
	# 	print('nihao')
	pass
y=You()
y.show()

#封装，私有属性、私有类的引入，python没有严格意义上的封装
import json
class Student(object):
	# 将类属性私有,特点__XXX
	__name = '张三'
	__age = 18
	# 将对象属性私有
	def __init__(self, sex, work):
		self.__sex = sex
		self.__work = work
	# 将实例方法私有
	def __play(self):
		print("偷偷玩王者荣耀")
def main():
	# print(dir(Student))
	# print(Student._Student__name) # 不推荐这种方式去访问
	s = Student(1, "Python")
	# print(s._Student__work) # 不推荐这种方式去访问
	# s._Student__play() # 不推荐这种方式去访问
if '__main__' == __name__:
	main()
'''
'''
# 构建学生类
class Student2(object):
	# 将类属性私有
	__name = '张三'
	__age = 18
	# 将对象属性私有
	def __init__(self, sex, work):
		self.__sex = sex
		self.__work = work
	def get_work(self):
		return self.__work
	@classmethod
	def get_name(cls):
		return cls.__name
	def get_play(self):
		return self.__play()
	def set_work(self,work):
		if work != 'Python':
			self.__work = 'Python'
		else :
			self.__work = work
	@classmethod
	def set_name(cls, name):
		cls.__name='name'
	# 将实例方法私有
	def __play(self):
		print("偷偷玩王者荣耀")
def main():
	
	s = Student2(1, "Java")
	print(s.get_work())
	print(Student2.get_name())
	s.get_play()

	# 错误代码演示 由于私有的关系，这种操作属于新增
	s = Student3(1, "Java")
	s.__name = '李四'
	print(dir(s))
	print(Student3.__dict__)
	print(s.__dict__)

	# 使用内部机制修改，不推荐
	s = Student2(1, "Java")
	s._Student2__name = '李四'
	print(s._Student2__name)
	
	# 使用 set_属性名方法修改
	s = Student2(1, "Java")
	s.set_work('Python')
	print(s.get_work())
	Student2.set_name('王五')
	print(Student2.get_name())
if '__main__' == __name__:
	main()


# 构建游戏类
class Game(object):
	def __init__(self):#无参
		self.__name = None
	def set_name(self, name):
		print("---setter, %s---"%name)
		self.__name = name
	def get_name(self):
		print("---getter---")
		return self.__name
	def del_name(self):
		print("----deleter---")
		del self.__name
	def __del__(self):
		print("我被释放了！")
# 接收变量 = property(get_属性名方法, set_属性名方法, del_属性名方法, "docstring")再次封装
	game = property(get_name, set_name, del_name, "这是一个游戏方法！")
def main():
	g = Game()
	g.game = "王者荣耀"
	print(g.game)
	del g.game
if '__main__' == __name__:
	main()
'''

''' 使用@property 装饰器
1. 在获取属性方法上添加@property
2. 获取属性、设置属性、删除属性三个方法名一致
3. 设置属性方法上和删除属性方法上使用一致的@方法名.xxx -> @name.setter，
@name.deleter
'''
# 构建游戏类
class Game3(object):
	def __init__(self):
		self.__name = None
	@property
	def name(self):
		print("---getter---")
		return self.__name
	@name.setter
	def name(self, name):
		print("---setter, %s---"%name)
		self.__name = name
	@name.deleter
	def name(self):
		print("---deleter---")
		del self.__name
	def __del__(self):
		print("我被释放了！")
def main():
	g = Game3()
	g.name = "王者荣耀"
	print(g.name)
	del g.name
if '__main__' == __name__:
	main()