# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

'''
FROM: 
https://www.py4e.com/tools/python-data/index.php?PHPSESSID=80e6aec79df2fe518c5a7525de076b62

Welcome Aleksandr Nezhelskiy from Using Python to Access Web Data

×Your answer is correct, score saved.
Extracting Data from XML

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_109327.xml (Sum ends with 21)
You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
Data Format and Approach
The data consists of a number of names and comment counts in XML as follows:

<comment>
  <name>Matthias</name>
  <count>97</count>
</comment>
You are to look through all the <comment> tags and find the <count> values sum the numbers. The closest sample code that shows how to parse XML is geoxml.py. But since the nesting of the elements in our data is different than the data we are parsing in that sample code you will have to make real changes to the code.
To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML for any tag named 'count' with the following line of code:

counts = tree.findall('.//count')
Take a look at the Python ElementTree documentation and look for the supported XPath syntax for details. You could also work from the top of the XML down to the comments node and then loop through the child nodes of the comments node.
Sample Execution

$ python3 solution.py
Enter location: http://py4e-data.dr-chuck.net/comments_42.xml
Retrieving http://py4e-data.dr-chuck.net/comments_42.xml
Retrieved 4189 characters
Count: 50
Sum: 2...
Turning in the Assignment

Enter the sum from the actual data and your Python code below:

'''



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

#Theanswer is 2521
