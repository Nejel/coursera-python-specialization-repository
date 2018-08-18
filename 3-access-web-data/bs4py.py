# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = ('http://py4e-data.dr-chuck.net/comments_109325.html')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
count = dict()
sum = int()

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    count[tag.contents[0]] = count.get(tag.contents[0], 0) + 1 # берем счетчик
    # на контент (там число) и складываем в словарь
    #print('Attrs:', tag.attrs)

#print(count)

for k, v in count.items() : # внутри словаря перемножаем значение и его счетчик
    sum += int(k) * int(v)

print(sum)
