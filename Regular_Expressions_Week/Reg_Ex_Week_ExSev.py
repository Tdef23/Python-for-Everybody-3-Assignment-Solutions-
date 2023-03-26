#Finding Numbers in a Haystack

#In this assignment you will read through and parse a file with text and numbers. 
#You will extract all the numbers in the file and compute the sum of the numbers.

#Actual data: http://py4e-data.dr-chuck.net/regex_sum_1290668.txt (There are 81 values and the sum ends with 218)

#Handling The Data

#The basic outline of this problem is to read the file, look for integers using the re.findall(), 
#looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers 
#and summing up the integers.

import re

try:
    fname = input('Enter file: ')
    fhand = open(fname)
    #fhand = open('Regular_Expressions_Week\\regex_sum_1290668.txt') alternate code to open file 
    #use 'Regular_Expressions_Week\\regex_sum_1290668.txt' as input if using above
except:
    print('File cannot be opened')
    quit()

numList = list() #create list

for line in fhand:
    line = line.rstrip()
    ns = re.findall('([0-9]+)', line) #expression code simplified
    for num in ns:                    #use for loop to append strings of numbers as integers in list form
        numList.append(int(num))
print(sum(numList))                   #use sum method to sum the integers from the file that have been appended to the list
fhand.close()                         #close file


