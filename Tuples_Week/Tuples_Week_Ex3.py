#Exercise 3: Write a program that reads a file and prints the 
#letters in decreasing order of frequency. Your program should
#convert all the input to lower case and only count the letters
#a-z. Your program should not count spaces, digits, punctuation,
#or anything other than the letters a-z. Find text samples 
#from several different languages and see how letter frequency
#varies between languages. Compare your results with the 
#tables at https://wikipedia.org/wiki/Letter_frequencies.

import string

counts = 0                          # Initialize variables
letter_freq = dict()
letter_f = list()

try:
    fname = input('Enter file name: ')
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    for character in string.punctuation:
        line = line.replace(character, '') 
    for character in string.digits:
        line = line.replace(character, '') #alternative lines of code using "replace" function instead of maketrans and translate below - worked for me
#    line = line.translate(line.maketrans('', '', string.punctuation)) #struggling to make this line of code and the one below work
#    line = line.translate(line.maketrans('', '', string.digits))
    words = line.lower().split()
    for word in words:
        for letter in word:
            # Count each letter for relative frequencies
            counts += 1
            letter_freq[letter] = letter_freq.get(letter, 0) + 1

for key, val in list(letter_freq.items()):
    letter_f.append((val / counts, key))  # Computes the relative frequency

letter_f.sort(reverse=True)         # Sorts from highest rel freq

for val, key in letter_f:
    print(key, val)
    #or print(key) as the instructions requested just the letter