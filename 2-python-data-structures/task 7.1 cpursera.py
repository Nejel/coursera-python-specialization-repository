# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname, 'r')
lines = list()
for line in fh:
    line = line.rstrip()
    lines.append(line)
fstr = str(lines)
print(open(fname, 'r').read().upper())



'''
fname = input("Enter file name: ")
fh = open(fname)
fw = open('write.txt', 'a')
lines = list()
for line in fh:
    line = line.rstrip()
    #line = line.strip()
    #line = line.upper()
    fw.write(line)
fstr = str(lines)
print(open('write.txt', 'r').read())
#print(fstr.upper())
'''


'''
fname = input("Enter file name: ")
fh = open(fname, 'r')
lines = list()
for line in fh:
    line = line.rstrip()
    lines.append(line)
fstr = str(lines)
print(fstr.upper())
'''



'''
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip()
fstr = str(fh)
print(fstr.upper)



'''
