# import pandas as pd
# # df = pd.read_csv('/home/shraddha/Desktop/codebeautify.tsv*', delimiter = '\t', quoting = 3)
# # df.head()
# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
# import re
# import nltk
# nltk.download('stopwords')
# from nltk.corpus import stopwords
# from nltk.stem.porter import PorterStemmer
# corpus = []
# for i in range(0, 3): 
#     review = re.sub('[^a-zA-Z]', ' ', df['headings'][i]) 
#     review = review.lower()
#     review = review.split()  
#     review = [word for word in review if not word in set(stopwords.words('english'))]
#     print(review)
   
    
#     corpus.append(review)
#  print(corpus)


#  //[['ease', 'business'], ['black', 'money'], ['fiscal', 'consolidation']]
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import xml.etree.ElementTree as ET
import lxml.etree
from bs4 import BeautifulSoup
import json
import os
import re

dir = 'E:\workspace\hackathon\seventeen'
directory = os.fsencode(dir)
# print(li)
li = list()
i=0
stringg = ""
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    print(filename)
    soup = BeautifulSoup(open(filename,'r',encoding="utf8"),"xml")
    head = soup.find('Heading').string
    string = string + " " + head

stop = set(stopwords.words('english'))

print([i for i in stringg.lower().split() if i not in stop])