import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location -- ') # Enter xml
print('Retrieving ', url)

xml = urllib.request.urlopen(url, context=ctx).read().decode() # read and decode xml
print('Retrieved ', len(xml), 'characters')

stuff = ET.fromstring(xml) # make xml as object / make it into a tree

lst = stuff.findall('comments/comment') # find element in the tree
print('Count ', len(lst))

char = []
sum = 0
for item in lst:
    char.append(item.find('name').text)
    sum += int(item.find('count').text)
print('sum: ', sum)
num_char = [len(i) for i in char]
