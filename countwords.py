input = "This is a test.  This is another test"
mydict = {}
with open("file.txt",'r') as f:
   textList = f.readlines()

for line in textList:
    lineList = line.split(" ")
    for word in lineList:
       if word in mydict.keys():
           mydict[word] = mydict[word] + 1
       else:
           mydict[word] = 1

for k,v in mydict.items():
    print("{0} occurs {1} times in the the input file".format(k,v))
