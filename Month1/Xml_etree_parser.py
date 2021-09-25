import xml.etree.cElementTree as et
#获取一颗xml树
tree=et.parse('Xml_practice6.xml')
#获取根节点
root=tree.getroot()
# print(root)
# 循环操作
for p in root:
	'''
	#增加节点，设置值
	sex_element=et.Element('sex')
	sex_element.text='男'
	p.append(sex_element)
	'''
	'''
	#修改文本
	for tname in p:
		# print(tname.tag,tname.text)
		if tname.tag=='test':
			if tname.text=='haha':
				tname.text='太帅了'
				tname.attrib['attr']='haha'
	'''
	#删除节点
	for tname in p:
		if tname.tag=='age':#只删一处
			p.remove(tname)
#重新写出xml文件
tree.write('Xml_practice7.xml',encoding='utf-8', xml_declaration=True)