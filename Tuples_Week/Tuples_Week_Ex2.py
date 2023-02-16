#Exercise 2: This program counts the distribution of the hour 
#of the day for each of the messages. You can pull the hour 
#from the "From" line by finding the time string and then 
#splitting that string into parts using the colon character. 
#Once you have accumulated the counts for each hour, print out 
#the counts, one per line, sorted by hour as shown below. 

#python timeofday.py
#Enter a file name: mbox-short.txt
#04 3
#06 1
#07 1
#09 2
#10 3
#11 6
#14 1
#15 2
#16 4
#17 2
#18 1
#19 1

try:                                  #open file
    fname = input('Enter file name:')
    fhand = open(fname)
except:
    print('File not found!')
    quit()

h_commits = dict()                    #establish dictionary
count = 0                             #establish beginning count
for line in fhand:                    #organize and parse
    words = line.split()
    if len(words) > 3 and words[0] == 'From':
        colpos = words[5].find(':')                 #split and identify position of hour
        hour = words[5][:colpos]
        h_commits[hour] = h_commits.get(hour,0) + 1 #establish counting for emails

h_counts = list()                       #estbalish list
for hour, count in h_commits.items():
    h_counts.append((hour, count))

h_counts.sort()             #sort list and print highest user count
for hour, count in h_counts:
    print(hour, count)

#Alternate
hcount = dict()                           #establish lists/dicts/tuples/counts
h_count = list()
count = 0

try:
    fname = input('Enter file name:')
    fhand = open(fname)
except:
    print('File cannot be opened')
    quit()

for line in fhand:
    words = line.split()
    if len(words) > 3 and words[0]=='From':
        colpos = words[5].find(':')        #identify position of colon
        hour = words[5][:colpos]           #segment hour from rest of time period and set
        hcount[hour]=hcount.get(hour,0) + 1

for hour, count in hcount.items():         #append from dict to list/tuple
    h_count.append((hour, count))

h_count.sort()                             #sort the list by hour

for hour, count in h_count:                #print tuple in correct form
    print(hour, count)
        
