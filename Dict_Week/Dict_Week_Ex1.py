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