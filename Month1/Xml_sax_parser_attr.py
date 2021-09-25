import xml.sax
class Peoson:
	#初始化对象
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def __str__(self):
		return 'Person name:{s.name},Person age:{s.age}'.format(s=self)

class Myhandler(xml.sax.handler.ContentHandler):#继承
	def __init__(self):
		self.persons=[]

	def startElement(self, tag_name, tag_attrs):
		if tag_name=='peoson':
			# print(tag_attrs['name'],tag_attrs['age'])
			self.persons.append(Peoson(tag_attrs['name'],tag_attrs['age']))

if __name__=="__main__":
	#创建xml解析器
	parser=xml.sax.make_parser()
	#关闭命名空间解析
	parser.setFeature(xml.sax.handler.feature_namespaces,0)
	#实例化对象
	myhandler=Myhandler()
	parser.setContentHandler(myhandler)
	#解析文档
	parser.parse('Xml_practice2.xml')
	for i in myhandler.persons:
		print(i)