import xml.etree.cElementTree as et
# a.通过root = et.Element("xml")创建一个root节点
root = et.Element('people')
# b.使用et.SubElement(root, 'FromUserName')创建子节点
peoson_element = et.SubElement(root, 'peoson')
name_element = et.SubElement(peoson_element, 'name')
name_element2 = et.SubElement(peoson_element, 'name')
age_element = et.SubElement(peoson_element, 'age')
age_element2 = et.SubElement(peoson_element, 'age')
attr_element=et.SubElement(peoson_element,'person')
# c.给子节点通过text属性填充内容
name_element.text = '熊大'
age_element.text = '13'
name_element2.text = '熊大'
age_element2.text = '13'
# 属性需要一次性添加，重复添加会覆盖原有
attr_element.attrib={'name':'翠花','age':'11'}
attr_element.attrib=dict(id='1234',sex='女')
# 也可以使用这样的操作，不过必须在字典之后
attr_element.attrib['身高']='180'
# d.使用tree = et.ElementTree(root)构建一颗树
tree = et.ElementTree(root)
# e.tree.write('xxx.xml', encoding="utf-8" , xml_declaration=True)写入文件 Ctrl+Alt+l格式化代码
#xml_declaration是否需要xml声明，short_empty_elements:True闭合标签、False成对标签
tree.write('Xml_practice6.xml', encoding='utf-8', xml_declaration=True)
