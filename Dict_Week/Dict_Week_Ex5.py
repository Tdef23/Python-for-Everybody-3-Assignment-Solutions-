#Exercise 5: This program records the domain name 
#(instead of the address) where the message was sent 
#from instead of who the mail came from (i.e., the whole
#email address). At the end of the program, print out the 
#contents of your dictionary. 

#python schoolcount.py
#Enter a file name: mbox-short.txt
#{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
#'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

try:
    fname = input('Enter file name:')
    fhand = open(fname)
except:
    print('File cannot be opened')
    exit()

domain_count = dict()
for line in fhand:
    words = line.split()
    if len(words) > 3 and words[0] == 'From':
        domain = words[1]
        ndomain = domain[domain.find('@')+1:]
        domain_count[ndomain] = domain_count.get(ndomain,0) + 1 
print(domain_count)

#Alternate code using functions to accomplish the same result
def getDomain(domain): 
    return domain[domain.find('@')+1:]

try:
    fname = input('Enter a file name: ')
    fhand = open(fname)
except:
    print('File not found')
    exit()

domain_count = dict()

for line in fhand:
    line = line.split()
    if len(line) > 3 and line[0] == 'From':
        domain = getDomain(line[1])
        domain_count[domain] = domain_count.get(domain,0) + 1

print(domain_count)