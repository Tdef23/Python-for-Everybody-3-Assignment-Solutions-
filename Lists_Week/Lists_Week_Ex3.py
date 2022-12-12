#Exercise 3: Rewrite the guardian code in the above example 
#without two if statements. Instead, use a compound logical
#expression using the and logical operator with a single if
#statement.

 
fhand = open('Rev.txt')
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'SELECT':
        continue
    print(words[2])