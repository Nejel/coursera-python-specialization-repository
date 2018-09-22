#Way 1
fname = input("Enter file name: ")
fh = open(fname, 'r')



#Way2
myfile = open('sample.txt') #this is class '_io.TextIOWrapper'
# dir(myfile) # way to look at available methods
content = myfile.read()
myfile.close()
print(content)



# Concept of the cursor
myfile.read() #read the lines by cursor
'apple\nbanana' #results
myfile.read() #read again
'' #because cursore at the down of the file, where is empty
myfile.seek(0) # get cursor back to start of the file
