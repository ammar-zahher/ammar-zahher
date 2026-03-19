import urllib.error,urllib.request,urllib.parse
from bs4 import BeautifulSoup
link=input("add link:")
b=urllib.request.urlopen(link).read()
reader=BeautifulSoup(b,"html.parser")
tags=reader("a")
for tag in tags:
    print(tag.get('href', None))
