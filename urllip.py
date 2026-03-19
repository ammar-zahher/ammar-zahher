import urllib.error,urllib.request,urllib.parse
j=dict()
link=input("add link:")
b=urllib.request.urlopen(link)
for line in b:
    m=line.decode().strip()
    n=m.split()
    for k in n:
        j[k]=j.get(k,0)+1
o=j.items()
mh=None #the most common word
jk=None #the name of the most repaeated word
# a is a word
# q is a count
for a,q in o:
    if jk is None or q>jk:
        jk=q
        mh=a
print(mh,jk)
