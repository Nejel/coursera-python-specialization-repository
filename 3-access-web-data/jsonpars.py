import json
from json import loads
import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import ssl
import re
from re import finditer


data = '''
[
    {
      "note":"This file contains the sample data for testing",
      "comments":[
        {
          "name":"Romina",
          "count":97
        },
        {
          "name":"Laurie",
          "count":97
        },
        {
          "name":"Bayli",
          "count":90
        },
        {
          "name":"Siyona",
          "count":90
        },
        {
          "name":"Taisha",
          "count":88
        },
        {
          "name":"Alanda",
          "count":87
        },
        {
          "name":"Ameelia",
          "count":87
        },
        {
          "name":"Prasheeta",
          "count":80
        },
        {
          "name":"Asif",
          "count":79
        },
        {
          "name":"Risa",
          "count":79
        },
        {
          "name":"Zi",
          "count":78
        },
        {
          "name":"Danyil",
          "count":76
        },
        {
          "name":"Ediomi",
          "count":76
        },
        {
          "name":"Barry",
          "count":72
        },
        {
          "name":"Lance",
          "count":72
        },
        {
          "name":"Hattie",
          "count":66
        },
        {
          "name":"Mathu",
          "count":66
        },
        {
          "name":"Bowie",
          "count":65
        },
        {
          "name":"Samara",
          "count":65
        },
        {
          "name":"Uchenna",
          "count":64
        },
        {
          "name":"Shauni",
          "count":61
        },
        {
          "name":"Georgia",
          "count":61
        },
        {
          "name":"Rivan",
          "count":59
        },
        {
          "name":"Kenan",
          "count":58
        },
        {
          "name":"Hassan",
          "count":57
        },
        {
          "name":"Isma",
          "count":57
        },
        {
          "name":"Samanthalee",
          "count":54
        },
        {
          "name":"Alexa",
          "count":51
        },
        {
          "name":"Caine",
          "count":49
        },
        {
          "name":"Grady",
          "count":47
        },
        {
          "name":"Anne",
          "count":40
        },
        {
          "name":"Rihan",
          "count":38
        },
        {
          "name":"Alexei",
          "count":37
        },
        {
          "name":"Indie",
          "count":36
        },
        {
          "name":"Rhuairidh",
          "count":36
        },
        {
          "name":"Annoushka",
          "count":32
        },
        {
          "name":"Kenzi",
          "count":25
        },
        {
          "name":"Shahd",
          "count":24
        },
        {
          "name":"Irvine",
          "count":22
        },
        {
          "name":"Carys",
          "count":21
        },
        {
          "name":"Skye",
          "count":19
        },
        {
          "name":"Atiya",
          "count":18
        },
        {
          "name":"Rohan",
          "count":18
        },
        {
          "name":"Nuala",
          "count":14
        },
        {
          "name":"Maram",
          "count":12
        },
        {
          "name":"Carlo",
          "count":12
        },
        {
          "name":"Japleen",
          "count":9
        },
        {
          "name":"Breeanna",
          "count":7
        },
        {
          "name":"Zaaine",
          "count":3
        },
        {
          "name":"Inika",
          "count":2
        }
      ]
    }
]'''


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


info = json.loads(data)
info2 = loads (data)

'''
#jdata = json.loads(open ('bookmarks.json').read())
for c in info['comments'][0]['name']:
#    print 'Title: {}, URI: {}'.format(c.get('title', 'No title'),c.get('uri', 'No uri'))

'''



'''


info = json.loads(data)
info2 = loads (data)

def function(json_object, name):
        return [obj for obj in json_object if obj['name']==name][0]['price']

function(info2, name)
'''

'''
info = json.loads(data)
info2 = loads (data)
print(info)
print(info2)

def jsonname (name):
    for entry in info2:
        if name == entry ['comments']:
            print('Go')
            #return entry ['comments']
            print(item['comments'][0]['count'])


jsonname(comments)
'''



'''
info = json.loads(data)

url = 'http://py4e-data.dr-chuck.net/comments_42.json'
uh = urllib.request.urlopen(url)
# reads = data.read()
# print(reads.decode())
# tree = ET.fromstring(reads)
print('User count:', len(info))

for item in info:
    # results = info.findall('comments')
    #dict = (item['comments'])
    #print(dict)
    for x in item:
        lat = item[0].find('count').text
        # lat = results[0].find('count').text
        # tag = item['comments'][0]['count']
        # print(tag)
        print(lat)
        #print('Count', item['count'])
    # print('Attribute', item['x'])

'''
'''
for item in info:
    #dict = (item['comments'])
    #print(dict)
    for x in item:
        tag = item['comments']+list(x)+['count']
        print(tag)
        #print('Count', item['count'])
    # print('Attribute', item['x'])
'''


sum = 0

for item in info:
    dict = ('Name', item['comments'])
    print(dict)
    for items in dict:
        string = str(items)
        print(string)
        #sum += (re.findall('\'count\': ([0-9]+)', string))
        line = (re.findall('\'count\': ([0-9]+)', string, flags=0))
        for x in line:
            sum += int(x)
            print(sum)

        # print('Count', items['comments'][1]['count'])
    # print('Count', item['count'])
    # print('Attribute', item['x'])
