# -*- coding: utf-8 -*-
# lesson 3.7: XML, library ElementTree, library lxml.
from xml.etree import ElementTree
from random import random
'''
tree = ElementTree.parse("example_copy.xml")
root = tree.getroot()
# use root = ElementTree.fromstring(string_xml_data) to parse from str

#print(root)
#print(root.tag, root.attrib)
#print(root[0][0].text)
#for child in root:
#	print(child.tag, child.attrib) 

#for element in root.iter("scores"):
#	score_sum = 0
#	for child in element:
#		score_sum += float(child.text)
#	print(score_sum)

greg = root[0]
#print(greg.attrib)
#module1 = next(greg.iter("module1"))
#print(module1, module1.text)
#module1.text = str(float(module1.text) + 30)

#certificate = greg[2]
#certificate.set("type", "with distinction")

#description = ElementTree.Element("description")
#description.text = "Showe excellent skills during the course"
#greg.append(description)

description = greg.find("description")
print(description)
greg.remove(description)

tree.write("example_copy.xml")
'''
'''
root = ElementTree.Element("student")
root.attrib = {"id":"1"}

first_name = ElementTree.SubElement(root, "firstName")
first_name.text = "Greg"

last_name = ElementTree.SubElement(root, "lastName")
last_name.text = "Dean"

certificate = ElementTree.SubElement(root, "certificate")
certificate.text = "True"

scores = ElementTree.SubElement(root, "scores")

for i in range(1,4):
	module = ElementTree.SubElement(scores, "module{}".format(str(i)))
	module.text = str(int(random()*100))

tree = ElementTree.ElementTree(root)
tree.write("file.xml")
'''
from lxml import etree
import requests
'''
response = requests.get("https://docs.python.org/3/")
print(response.status_code)
print(response.headers["Content-Type"])

parser = etree.HTMLParser()
root = etree.fromstring(response.text, parser)

for element in root.iter("a"):
	print(element, element.attrib)
'''
from xml.etree import ElementTree

xml_data = input()

root = ElementTree.fromstring(xml_data)

def getpricecolor(root, color, price = 0):
	pass

def printelements(root, tab="\t", counttab=0):
	string = "{}{} {}".format(tab*counttab, root.tag, root.attrib["color"])
	print(string)
	for element in root:
		try:
			printelements(element, counttab=counttab+1)
		except TypeError:
			pass

for out in printelements(root):
	print(out)