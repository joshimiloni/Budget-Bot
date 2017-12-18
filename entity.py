import xml.etree.ElementTree as ET
import lxml.etree
from bs4 import BeautifulSoup
import os


dir = 'E:\workspace\hackathon\GST'
directory = os.fsencode(dir)
# print(li)
li = list()
i=0
entity = {}

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    print(filename)
    soup = BeautifulSoup(open(filename,'r',encoding="utf8"),"xml")
    head = soup.find('Heading').string
    entity["value"] = head
    print(entity)
