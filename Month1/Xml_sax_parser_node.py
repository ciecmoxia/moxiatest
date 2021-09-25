import xml.sax
# 创建一个类继承ContentHandler
class MyHandler(xml.sax.handler.ContentHandler):#alt+insert
	def __init__(self):
		self.name=''
		self.age=0
		self.current_tag=''#当前节点
	#1.开始解析元素的调用方法，重写
	#只解析name和age
	def startElement(self, tag_name, tag_attrs):#attrs属性
		#print('解析开始：',tag_attrs,tag_name)
		if tag_name=='name':
			#print(tag_name)
			self.current_tag=tag_name#中转站接收

		if tag_name=='age':
			#print(tag_name)
			self.current_tag=tag_name

	#3.结束解析元素的调用方法，重写
	def endElement(self, tag_name):
		#print('解析结束：',tag_name)
		if tag_name=='name':
			print('Person name:',self.name)

		if tag_name=='age':
			print('Person age:',self.age)

	#2.获取内容的调用方法，重写
	def characters(self,content):
		#print('获取内容：',content)
		if self.current_tag=='name':
			#print(content)
			self.name=content

		if self.current_tag=='age':
			#print(content)
			self.age=content

if __name__ == '__main__':
	# 创建xml reader
	parser = xml.sax.make_parser()
	# 关闭命名空间解析
	parser.setFeature(xml.sax.handler.feature_namespaces,0)#0是state的意思
	#实例化解析对象
	handler=MyHandler()
	parser.setContentHandler(handler)
	# 解析xml文档
	parser.parse('Xml_practice.xml')