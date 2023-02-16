#Exercise 1: Revise a previous program as follows: Read and
#parse the "From" lines and pull out the addresses from 
#the line. Count the number of messages from each person 
#using a dictionary. 

#After all the data has been read, print the person with the
#most commits by creating a list of (count, email) tuples 
#from the dictionary. Then sort the list in reverse order 
#and print out the person who has the most commits. 

#Sample Line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

#Enter a file name: mbox-short.txt
#cwen@iupui.edu 5

#Enter a file name: mbox.txt
#zqian@umich.edu 195

import os
import string

try:                                  #open file
    fname = input('Enter file name:')
    fhand = open(fname)
except:
    print('File not found!')
    quit()

m_commits = dict()                    #establish dictionary
count = 0                             #establish beginning count
for line in fhand:                    #organize and parse
    words = line.split()
    if len(words) > 3 and words[0] == 'From':
        email_user = words[1]
        m_commits[email_user] = m_commits.get(email_user,0) + 1 #establish counting for emails

counts = list()                       #estbalish list
for email, count in m_commits.items():
    counts.append((count, email))

counts.sort(reverse=True)             #sort list and print highest user count
for count, email in counts[:1]:
    print(email, count)