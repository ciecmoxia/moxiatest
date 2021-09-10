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
	# 将实例方法私有
	def __play(self):
		print("偷偷玩王者荣耀")
def main():
	s = Student2(1, "Java")
	print(s.get_work())
	print(Student2.get_name())
	s.get_play()
if '__main__' == __name__:
	main()