'''
import copy
a='123'
b=a
print(id(a),id(b))
a1=(1,2,3)
# b1=a1.copy()
b1=copy.deepcopy(a1)
print(id(a1),id(b1))

cart =['sxt', ['bjsxt', 'shsxt']]
cart2 = cart # 地址拷贝
print(id(cart)) # 拷贝引用而已
print(id(cart2))
# 浅拷贝，仅拷贝外层内容，不拷贝内层
cart =['sxt', ['bjsxt', 'shsxt']]
cart_shallow = cart.copy()
print(id(cart[1]))
print(id(cart_shallow[1])) # 地址相同
cart_shallow[1].append('change') # 会更改原有的列表
智者乐水 仁者乐山 程序员 乐字节 45 如果需要更多优质的Java、Python、架构、大数据等IT资料请加微信：lezijie007
print(cart)
或者使用
import copy
cart =['baidu', ['sina', 'qq']]
deep_copy = copy.deepcopy(cart) # 深表复制，地址和内容都
变
deep_copy[1].append('ml')
print(deep_copy)
print(cart) # 不影响变化
注意:如果是元组，元组时不可改变的，因此都是拷贝不了
import copy
fruits =('apple','pear')
fruits_copy = copy.copy(fruits) #不可变对象不能拷贝，直接指
向原对象
print(id(fruits))
print(id(fruits_copy))
'''
test_list=['day','day','up']
for i in range(0,len(test_list)):
	print(i,test_list[i])

j=0
for element in test_list:
	print(j,test_list[j])
	j+=1

for i,e in enumerate(test_list):#枚举
	print(i,e)

for i,j in enumerate('abc'):#字符串也是一种容器
	print(i,j)

l=[]
for x in range(1,6):
	l.append("{}*{}".format(x,x))
print(l)
l1=["%d*%d"%(x,x) for x in range(1,6)]#列表生成式
print(l1)

l2=[x for x in range(1,6) if x%2==0]#返回偶数
l3=[x for x in range(1,6) if x%2==1]#返回奇数
print(l2,l3)

l4=[x if x>2 else 0 for x in range(1,6) if x%2==1]
print(l4)

word=['Java','Python','C++',123]
print([s.lower() if isinstance(s,str) else s for s in word])#转小写

print('\n'.join(['  '.join(['{}*{}={:<2}'.format(c,r,c*r) for c in range(1,r+1)]) for r in range(1,10)]))#九九乘法表，{:<2}占位2位

l5=("%d*%d"%(x,x) for x in range(1,6))#列表生成式(),()作用：运算符，元组，列表生成器
print(l5)#返回类型，不返回值
#print(next(l5))#只返回一个，惰性
for i in range(1,6):
	print(next(l5),end=" ")#默认换行，用空格代替

'''
from collections import Iterator#迭代器
gen = (n for n in range(1,5))
next(gen) # 迭代器对象可以丢入 next()方法中
isinstance(gen,Iterator) # 查看是否为迭代的对象
isinstance({},Iterator) #false可以通过 iter()函数，将可迭代的对象包装成迭代器，如
str_iter=iter('sxt')
next(str_iter)
next(str_iter)
next(str_iter) sxt_dict ={'name':'老王', 'sex':1, 'address':'隔壁', 'address':'松江'}
dict_iter=iter(sxt_dict)
next(dict_iter)
next(dict_iter)
next(dict_iter)
Iterable 与 iterator 的关系，就相当于机器人与人，但是不是
真正的人，仅仅具有走的功能而已，可给机器人穿衣服打扮
成人的样子，所以说具有迭代功能的不一定是迭代器

from collections import deque # 从内置的模块中引入双向队列
dq = deque(['sxt', 'aa', 'bb'])
dq.append('msb')
dq.appendleft('laopei')

from collections import namedtuple # 从内置的模块中引入
Person = namedtuple('Person', ['name', 'age'])
p = Person("laopei",18)
print(p.age,p.name)

from collections import OrderedDict # 从内置的模块中引入
all = dict([('shsxt1', 1), ('bj', 2), ('sh', 3)])
all # 不是按存放的顺序
odict = OrderedDict([('shsxt1', 1), ('bj', 2), ('sh',3)])
odict # 按存放的顺序
odict = OrderedDict()
odict ['s'] = 'shsxt'
odict ['b'] = 'bjsxt'
odict ['c'] = 'cssxt'
print(odict)

from collections import Counter
msg = 'talk is cheap show me the code show me the code'
letters = msg.split(" ")
counter = Counter()
for l in letters :
counter[l] =counter[l]+1
for k,v in counter.items():
print(k,v)
'''