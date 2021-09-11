'''
	python先__new__方法开辟空间
	继承：子承父业
	a. 沿用父类信息
	b. 重写父类信息
	c. 新增自己信息
	格式：
	class F(object):
		pass
	class C(F):
		pass
'''

'''
# 继承
class Person(object):
	age = 18
	def __new__(cls):#一般情况下不要自己重写__new__方法，写错了就会无法开辟空间
		print("调用父类 Person 开辟空间")
		return object.__new__(cls)
# 重写父类 object 的__init__
	def __init__(self):
		print("调用父类 Person 初始化方法")

class User(Person):
	def __new__(cls, name):#__new__方法也可以使用__init__的赋值，不过得cls.XXX=XXX,__new__必须和__init__方法的参数一致
		print("调用 User 自己开辟空间")
		# return Person.__new__(cls)
		return object.__new__(cls)
# 重写父类 Person 的__init__
	def __init__(self, name):
		print("调用 User 自己的初始化方法")
		self.name = name
u = User('张三')
print(u.age)
Person.sex = 1
print(u.sex)
#就近原则：自己没有找父亲，向上追溯继承链

# 判断子类
class Parent(object):
	pass
class Child(Parent):
	pass
c = Child()
# 判断子类 是它 是它 都是它 我们的根类 object
print(isinstance(c, Parent))
print(isinstance(c, object))
print(isinstance(Parent, object))
print('*'*30)
# 判断引用
c1 = c
print(c1 is c)
print(c1 is Child())
print(c1 is Parent())
print('*'*30)
# 判断子类
print(issubclass(Child, Parent))
print(issubclass(Child, object))
print(issubclass(Parent, object))

# 私有
class Parent(object):
	def __init__(self, name):
		self.__name = name
	def get_name(self):
		return self.__name
	def somke(self):
		return self.__somking()
	def __somking(self):
		print("爱抽烟")
# 单继承
class Child(Parent):
	pass
c = Child("老王")
c.somke()

# 私有
class Parent(object):
	def __init__(self, name):
		self.__name = name
	def get_name(self):
		return self.__name
	def somke(self):
		return self.__somking()
	def __somking(self):
		print("爱抽烟")
# 单继承
class Child(Parent):
# 重写
	def somke(self):     #super() -> 指向调用者的父类
	#super().somke() # 我就想抽一口
		super(Child, self).somke()
		print("未成年不允许抽烟")
c = Child("小明")
c.somke()


class User(object):
	def __new__(cls, name, age):
		print("开始创建父类对象")
		cls.name=None
		cls.age=None
		return object.__new__(cls)

	def __init__(self,name, age):
		print("开始初始化父类对象")
		self.name=name
		self.age=age

class Sub(User):
	def __new__(cls, name,age,gender):
		print("开始创建子类对象")
		cls.gender = None
		return object.__new__(cls)

	def __init__(self, name, age,gender):
		print("开始初始化子类对象")
		super(Sub, self).__init__(name,age)
		self.gender=gender

u=User("mike",38)
print("print your name:",u.name)
s=Sub("mical",16,"男")
print("print your gender:",s.gender)
print("print your name:",s.name)#print your name: None
'''
#定制方法
class User:
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def __repr__(self):
		print("调用repr方法",self.__dict__)
		return str(self.__dict__)

	def __str__(self):
		print("调用str方法",self.__dict__)
		return str(self.__dict__)

	def __hash__(self):
		return hash((self.name,self.age))

	def __call__(self, friend):
		print("把方法当函数使用:",self.name,"喜欢",friend)

	def __getattribute__(self, name):#!
		print('拦截所有获取属性的语句')
		return object.__getattribute__(self,name)

	def __getattr__(self, sstr):
		print('获取没定义的属性')
		return sstr

	def __setattr__(self, key, value):
		print('拦截所有设置属性的语句')
		object.__setattr__(self,"haha"+key,value)

	def __delattr__(self, name):
		if name in ['name','pages']:
			print("拦截所有删除属性的语句")
			return
		object.__delattr__(self,name)

u=User("jack",18)
u_str=repr(u)
#u_str=str(u)
print(hash(u))
u('lose')
print(u.ss)
print(u.aha_name)
print(u_str,type(u_str))
u_obj=eval(u_str)#字符串转字典
print(u_obj['name'],type(u_obj))