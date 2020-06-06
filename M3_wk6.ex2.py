import urllib.request, urllib.parse, urllib.error
import ssl
import json
import twurl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = input('Enter API Key -- ')
if len(api_key) < 1:
    api_key = False
    if api_key is False:
        api_key = 42
        serviceurl = 'http://py4e-data.dr-chuck.net/json?' # static api for geo coding
    print('API Key: ', api_key)
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?' # default api from google for geo coding
    print('API Key: ', api_key)

while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    parms = dict() # create empty dict
    parms['key'] = api_key # add in address as key and use input above as value
    parms['address'] = address
    url = serviceurl + urllib.parse.urlencode(parms) # encode the value and concatenate with the serviceurl for retrieving geo data
    print('Retrieving ', url)
    uh = urllib.request.urlopen(url, context=ctx) # open the concatenated url
    data = uh.read().decode()
    print('Retrieved ', len(data), 'characters')

    # return None if data is not retrieved due to error during parsing
    try:
        js = json.loads(data)
    except:
        js = None

    # if status has error then print the error and continue the loop
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure to retrieve data ===')
        print(data)
        continue

    #print(json.dumps(js, indent=4)) # Adjust indent to make it easier to read the retrieved json data
    place_id = js['results'][0]['place_id']
    print('Place id:', place_id)



