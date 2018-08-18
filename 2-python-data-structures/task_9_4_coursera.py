'''
9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

name = input("Enter file:")
if len(name) < 2 : name = "mbox-short.txt"
handle = open(name)

di = {}
counter = 0
diction = dict()
str = 'From '
str2 = '@'

for lines in handle :
    lines = lines.rstrip()
    wds = lines.split()
    for word in wds:
        if lines.startswith(str) and word.find(str2) != -1 :
        # if word.find(str) != -1 : # тут над на регулярке написать условие для поиска по паттерну From edu@edu.com
            di[word] = di.get(word, 0) + 1 # idiom: retrive\create\update counter
        # print(word, 'new!', di[word]) #print just for sure that everithyng is ok
        # Code below is dong the same
        '''
        if word in di:
            di[word] = di[word] + 1
            counter += 1
        else:
            di[word] = 1
            counter += 1
        print(word)
        '''



# Now we are going to find the most common words

largest = -1
theword = None

for k,v in di.items() :
    if v > largest:
        largest = v
        theword = k

print(theword, largest)

'''
    words = lines.split() # либо тут удаляется пробел после Фром
    for word in words:
        wordstr = str(words)
        wordstr.split() # либо тут удаляется пробел после Фром
        if not wordstr.startswith('From') : continue # либо тут ошибка
        diction[wordstr] = diction.get(wordstr, 0) + 1 # dict.get(key, default = None) key − This is the Key to be searched in the dictionary. default − This is the Value to be returned in case key does not exist.
        counter += 1
    #diction[words] = diction[words] + 1
    # осталось посчитать частоту и вывести это
'''
