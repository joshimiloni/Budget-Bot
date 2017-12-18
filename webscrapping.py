import time
import timeout_decorator

@timeout_decorator.timeout(864000)
def mytest():
    print "Start"
    for i in range(1,9000000):
        time.sleep(1)
        print "%d seconds have passed" % i

if __name__ == '__main__':
    #mytest()



from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url='https://cleartax.in/s/gst-news-and-announcements'
uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")
uClient.close()
container=page_soup('div',{"style":"padding: 40px; margin: 20px 0; border: 1px solid #ccc; background: #fafafa; text-align: justified;"})
container[0]
item1=container[0].ul
item1= item1.findNext('ul').findNext('ul').findNext('ul')
string = ""
print(item1)
item=list()
it = {}
for li in item1.findAll('li'):
    ul=li.get_text()
    
    it["value"]=ul

    string = string + " " + it
print(string)
