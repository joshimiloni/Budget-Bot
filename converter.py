import xml.etree.ElementTree as ET
import lxml.etree
from bs4 import BeautifulSoup
import json
import os

dir = 'E:\workspace\hackathon\sixteen'
directory = os.fsencode(dir)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    print(filename)


soup = BeautifulSoup(open('demo3.xml','r'),"xml")

head = soup.find('Heading').string
summary = soup.find('Summary').string
url = soup.find('URL').string
print(summary)
term = '"' + head + '"'
temp = list()
temp.append(head)
context = head.replace(" ","-")
print(context) 
string = " FOR MORE INFO VIST: "
final = summary + string + url
print(final)
# head = '[' + term + ']'
# print(head)
i = 7
stringg = str(i)
f = open("demo"+stringg+".json", "w+")
jsonFile = open("demo.json", "r+")
data = json.load(jsonFile)


tmp = data["templates"]
data["templates"] = temp

tmp1 = data["name"]
data["name"] = head

for list in data["responses"]:
	print(list["speech"])
	tmp1 = list["speech"]
	list["speech"] = final
	for l in list["affectedContexts"]:
		# print(l["name"])
		tmp2 = l["name"]
		l["name"] = context

f.write(json.dumps(data))