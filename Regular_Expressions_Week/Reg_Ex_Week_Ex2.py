#Exercise 2: Write a program to look for lines of the form: 

#New Revision: 39772 

#Extract the number from each of the lines using a regular expression and the findall() method. Compute the average of the numbers 
#and print out the average. 

#Enter file:mbox.txt
38444.0323119

#Enter file:mbox-short.txt
39756.9259259

import re

try:
    #fname = input('Enter file: ')
    fhand = open('Regular_Expressions_Week\\mbox.txt')
except:
    print('File cannot be opened')
    quit()

nrSearch = '^New Revision: ([0-9.]+)' #establish expression code to find
match = 0 #establish count
sum = 0 #stablish sum

for line in fhand:
    line = line.strip()
    nr = re.findall(nrSearch, line) #expression code simplified
    if len(nr) > 0:
        sum = int(nr[0]) + sum #conduct sum
        match += 1 #start match
    
average = sum/match
print(average)