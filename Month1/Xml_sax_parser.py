import xml.sax
# 创建一个类继承ContentHandler
class MyHandler(xml.sax.handler.ContentHandler):#alt+insert
	#开始解析元素的调用方法，重写
	def startElement(self, tag_name, tag_attrs):
		print('解析开始：',tag_attrs,tag_name)

	# 结束解析元素的调用方法，重写
	def endElement(self, tag_name):
		print('解析结束：',tag_name)

	# 获取内容的调用方法，重写
	def characters(self,content):
		print('获取内容：',content)

if __name__ == '__main__':
	# 创建xml reader
	parser = xml.sax.make_parser()
	# 关闭命名空间解析
	parser.setFeature(xml.sax.handler.feature_namespaces,0)
	#实例化解析对象
	handler=MyHandler()
	parser.setContentHandler(handler)
	# 解析xml文档
	parser.parse('Xml_practice.xml')