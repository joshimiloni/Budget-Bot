import json
import os


dir = 'E:\workspace\hackathon\seventeen'
directory = os.fsencode(dir)
# print(li)
li = list()
i=0
entity = {}

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    # print(filename)
    soup = BeautifulSoup(open(filename,'r',encoding="utf8"),"xml")
    cat = soup.find(Category).string
    url = soup.find(URL).string
    entity["cat"] = cat
    entity["url"] = url
    li.append(entity.copy())
print(li)