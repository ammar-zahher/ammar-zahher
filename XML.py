import xml.etree.ElementTree as ET
data="""
<stuff>
    <user number="03">
       <id>0245</id>
       <name>Ammar</name>
    </user>
    <user number="09">
       <id>4088</id>
       <name>hesham</name>
    </user>
</stuff>"""
mk=ET.fromstring(data)
mg=mk.findall("user")
print("user account:",len(mg))
for item in mg:
    print(item.get("number"))
    print(item.find("name").text)
    print(item.find("id").text)
    
