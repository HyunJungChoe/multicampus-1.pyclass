import urllib.request
from bs4 import BeautifulSoup

url = "https://www.naver.com"
html = urllib.request.urlopen(url)
bs_obj = BeautifulSoup(html, "html.parser")
ul = bs_obj.find("ul",{'class':'an_l'})
#print(ul)
lis = ul.findAll('li')
for li in lis:
    a_tag = li.find('a')
    #print(a_tag)
    span = a_tag.find('span', {'class':'an_txt'})
    print(span.text)

