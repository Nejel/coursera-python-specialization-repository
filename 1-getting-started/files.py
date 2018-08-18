'''

Coursera Python. Course 2. Week 3.  Video 1.
FILES.
https://www.coursera.org/learn/python-data/lecture/6x7OZ/7-1-files

'''


# open files:
fhand = open('text.txt', 'r') # read the fileself.
#fhand = open('text.txt') # read properties of file
print(fhand)


# quantity of symbols:
stuff = "X\nY" # 3 symbols from the Python point of view
print(stuff)


# printing lines:
xfile = open('box.txt')
for cheese in xfile:
    print(cheese)


# counting lines:
fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count: ', count)

### OUTPUT
# $python open.py
# Line Count: 134366


# Reading the WHOLE file:
fhand = open('mbox2.txt')
inp = fhand.read()
print(len(inp))
# 95634
print(inp[:20]) # print first 20 symbols
# From stephen.marquar


# read lines if they starts with some text
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip() # delete one unneeded \n from the end of the line. Just to prevent douled perenosy.
    if line.startswith('From'):
        print(line)


# If line NOT starts with
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip() # delete one unneeded \n from the end of the line. Just to prevent douled perenosy.
    if not line.startswith('From'): # <---- THIS
        continue
    print(line)


# We can look for a string anywhere in  line as our selection criteria
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip() # delete one unneeded \n from the end of the line. Just to prevent douled perenosy.
    if not 'some text here' in line: # <---- THIS
        continue
    print(line)


# Open files

fname = input('Enter the file name to open in up: ')
try:
    fhand = open(fname)
except:
    print('File cannot be found or opened in that directiory: ', fname)
    quit()

count = 0
for line in fhand:
    if line.startwith('Subject: ') :
        count = count + 1
    print('There were', count, 'subject lines in', fname)


#TAKS 7.1
#https://www.py4e.com/tools/pythonauto/?PHPSESSID=cc11dc62f7f5799b3c311e8b7c50d446
# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname, 'r')
lines = list()
for line in fh:
    line = line.rstrip()
    lines.append(line)
fstr = str(lines)
print(open(fname, 'r').read().upper())
