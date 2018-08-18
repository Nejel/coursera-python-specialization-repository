'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''

name = input("Enter file:")
if len(name) < 2 : name = "mbox-short.txt"
handle = open(name)

tuple = ()
list = []
di = {} # dictionary
string = ''
str = 'From '
str2 = ':'
counter = 0 # integer
float = 1.1 # float

for lines in handle :
    lines = lines.rstrip()
    wds = lines.split()
    for word in wds:
        if lines.startswith(str) and word.find(str2) != -1 :
            hour = word[0:2]
            di[hour] = di.get(hour, 0) + 1 # idiom: retrive\create\update counter

#print(di)
# print(sorted([ (v,k) for k,v in di.items()], reverse = True))
# print(sorted(di.items(), reverse = False))
sotreddi = (sorted(di.items(), reverse = False)) #Autograder tend not to read True of False and make reverse parameter True all the time. Just delete it.
for k,v in sotreddi:
    print(k,v)


'''
c = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
tmp = list()
for k, v in c.items() :
    tmp.append( (v, k) )

print(tmp)
'''
