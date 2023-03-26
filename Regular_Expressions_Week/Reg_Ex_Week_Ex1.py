#Exercise 1: Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter a regular expression 
#and count the number of lines that matched the regular expression: 

#$ python grep.py
#Enter a regular expression: ^Author
#mbox.txt had 1798 lines that matched ^Author

#$ python grep.py
#Enter a regular expression: ^X-
#mbox.txt had 14368 lines that matched ^X-

#$ python grep.py
#Enter a regular expression: java$
#mbox.txt had 4175 lines that matched java$

import re

handle = open('Regular_Expressions_Week\\mbox.txt') #open file

searchTerm = input('Enter regular expression:') #initialize input for term you want to count

expCount = 0 #initialize count

for line in handle:
    line = line.strip()
    if re.search(searchTerm, line): #use regular expression code to sift through term you want to find
        expCount += 1 #count

print('mbox.txt had',expCount,'lines that matched', searchTerm) #organize and print proper return