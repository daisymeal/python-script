from bs4 import BeautifulSoup #to get everything
import lxml
import requests
import re
import html 


print("testing")
f = open('data.txt','w')

fget = requests.get("https://data.fivethirtyeight.com/")
fsoup = BeautifulSoup(fget.text,'lxml')

fsoupl = fsoup.prettify()
body = fsoup.body

alltags = fsoup.find_all(True)

tab = open('web.csv', 'w')

for tag in alltags:
    f.write(str(tag.contents))
    tab.write(str(tag.contents))
