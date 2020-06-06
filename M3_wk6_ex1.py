import urllib.request, urllib.parse, urllib.error
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location -- ')
print('Retrieving ', url)

re_json = urllib.request.urlopen(url, context=ctx).read().decode()
print('Retrieved ', len(re_json), 'characters')

info = json.loads(re_json)
comments = info['comments']
print('Count:', len(comments))
sum = 0
for i in range(len(comments)):
    sum += comments[i]['count']
print('Sum: ', sum)
