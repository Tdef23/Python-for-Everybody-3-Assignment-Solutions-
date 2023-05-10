#Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the document from a URL, 
#(2) displaying up to 3000 characters, and (3) counting the overall number of characters in the document. 
#Don't worry about the headers for this exercise, simply show the first 3000 characters of the document 
#contents.

#Step 1: Refer to parts of urrlib code from Severance book pages 248-251
#Step 2: import urllib.request
#Step 3: enter line of code to open and read url through urllib request
#Step 4: enter get code above url open to enter/receive url - run code to see if it works
#Step 5: enter line of code below url open line to decode, I think urllib automatically encodes
#Step 6: enter line of code at bottom to print content of opened url to include up to 3000 characters
#Step 7: enter line below that to print count len of content

import urllib.request 

url = input('Enter URL: ')
internal = urllib.request.urlopen(url).read() #context = ctx not needed
internal = internal.decode() 

print(internal[:3000])
print(len(internal))

#We should get less characters as the result then the prior exercises because
#urllib does not need the header/otherinfo, it already takes care of that when
#reading and/or displaying the result





