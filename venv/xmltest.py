import os
import xml.etree.ElementTree as ET

data = ET.Element('data')
items = ET.SubElement(data, 'items')
item1 = ET.SubElement(items, 'item')
item2 = ET.SubElement(items, 'item')
item1.set('name','item1')
item2.set('name','item2')
item1.text = 'item1abc'
item2.text = 'item2abc'


mydata = ET.tostring(data)
mydata2 = str(mydata.decode('utf-8'))
myfile = open('test.xml', "w")
myfile.write(mydata2)