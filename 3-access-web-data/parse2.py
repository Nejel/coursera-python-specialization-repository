# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
sum = 0
import ssl
import re
pagecount = 0
tagcount = 0
html2 = ()
currenttag = ()
sampleurl = 'http://py4e-data.dr-chuck.net/comments_42.xml'
mainurl = 'http://py4e-data.dr-chuck.net/comments_109327.xml'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#url = ('http://py4e-data.dr-chuck.net/known_by_Harris.html')
url = mainurl


#html = urllib.request.urlopen(url).read()

# Retrieve all of the anchor tags
#while pagecount < 7 :
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('count')
for tag in tags:
    if tagcount < 7777:
        #print(tag.get('href', None))
        print(tag.string)
        sum += int(tag.string)
        tagcount += 1
        #print(tagcount)
        '''
        elif tagcount == 17:
            print(tag.get('href', None))
            currenttag = (tag.string)
            print(currenttag)
            #answer = re.findall('>(.)</a>', currenttag, flags = 0)
            #print(answer)
            url = (tag.get('href', None))
            break
        '''

#    pagecount += 1
#    tagcount = 0
#    continue
#else:
print(currenttag)
print(sum)
