import urllib.request
import xml.etree.ElementTree as ET
url=input("Enter URL:")
data=urllib.request.urlopen(url).read()
xml_tree=ET.fromstring(data)
counts=xml_tree.findall(".//count")
total_sum=0
for count in counts:
    count=int(count.text)
    total_sum=total_sum+count
print(total_sum)
