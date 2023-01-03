#Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt Write a program that reads the words in words.txt and stores 
#them as keys in a dictionary. It doesn't matter what the values are. Then you can use the in operator as a fast way to check whether 
#a string is in the dictionary.

try:
    fname = input('Enter file name:')
    fhand = open(fname)
except:
    print('File not Found')
    exit()

count = 0
file_dictionary = dict()                   #creates dictionary

for line in fhand:
    words = line.split()
    for word in words:
        count += 1
        if word in file_dictionary:
            continue                       #eliminates duplicates
        file_dictionary[word] = count      #makes word a key and the count a value (count is optional since value isn't important)

print(file_dictionary)                     #prints dictionary

if 'data' in file_dictionary:              #check whether string/key/word is in dictionary
    print('True')
else:
    print('False')