#简单的多选择
import random
hour = random.randint(6,14)
print("当前时间：%d"%hour)
if hour == 7:
	print("吃早点")
elif (hour == 10 or hour == 12):
	print("chiwufan")
else:
	print("上课")

month=random.randint(1,12)
mon=month//3
print("随机生成的月份：%d"%month,end="月")
if   mon == 1 :
	print('春天')
elif mon == 2 :
	print('夏天')
elif mon == 3 :
	print('秋天')
else :
	print('冬天')

#简单的循环
rand=random.randint(1,10)
#print("你的数是：%d"%rand)
'''while True :
	number = int(input("请输入："))
	if rand > number :
		print('太小')
	elif rand < number:
		print("太大")
	else :
		print("正好")
'''
num=0
'''
while num < 5 :
	print("hello%d"%num)
	num+=1
print("end")

while num < 5 :
	print("xxx")
	break
while 1==1:
	print("qqq")

while num<3:
	print("***")
	if num==2:
		continue
	num+=1
'''
#双重循环
row=9
while num < 5:
	i=0
	while i <= num:
		print("*",end="")
		i += 1
	print()
	num += 1
while num<9:
	j=9
	while j > num:
		print("*",end="")
		j=j-1
	print()
	num+=1

r=1
while r<=9:
	c=1
	while c<=r:
		print("%d * %d = %d" % (c, r, r * c), end="  ")
		c+=1
	print()
	r+=1

#for循环
'''
for i in range(1,11,1):#1-11左闭右开，第三个参数是步长
	print(i)
for x in range(11,0,-1):
	print(x)
'''
for row1 in range(1,10):
	for col1 in range(1,row1+1):
		print("{}*{}={}".format(col1,row1,row1*col1),end="  ")
		#print("%d*%d=%d"%(col1,row1,row1*col1),end="  ")
	print()

num1=1
sum=0
'''
while num1<=10:
	sum=sum+num1
	num1 += 1
print(sum)

num2=int(input("输一个数："))
for n in range(1,num2+1):
	sum+=n
print(sum)

#m=int(input("传参："))
def leijia(m):
	i=0
	sum=0
	while i<=m:
		sum=sum+i
		i +=1
	return sum
def leicheng(n):
	i=1
	che=1
	while i<=n:
		che=che*i
		i+=1
	return che
print(leijia(10))
print(leicheng(5))
'''
a="sjkldn"#字符串
print(type(a))
b=[1,1.5,1,"a","hdsakld"]#列表，有序，可重复、可变
print(type(b))
c=(1,1.5,1,"a","hdsakld")#元组，有序、可重复、不可变
c1=[1,[1.5],[1,"a"],"hdsakld"]
print(type(c),type(c1))
d=set([1,1.5,1,"a","hdsakld"])#集合，无序、不重复
e=set((1,1.5,1,"a","hdsakld"))
print(d,e)
f={1,1.5,1,"a","hdsakld"}
print(type(d),type(e),type(f))
g={'a':12,'b':"[1,x]",'c':(["sgav","gashjg"])}#字典，键值对，键不可重复
print(type(g))
