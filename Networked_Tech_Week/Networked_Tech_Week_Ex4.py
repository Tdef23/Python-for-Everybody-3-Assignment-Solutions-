#Exercise 4: Change the urllinks.py program to extract and count paragraph (p) tags 
#from the retrieved HTML document and display the count of the paragraphs as the output 
#of your program. Do not display the paragraph text, only count them. Test your program 
#on several small web pages as well as some larger web pages.

#Step 1: Make sure BeautifulSoup is installed and it is attached to the folder
#you are using for the exercise

#Step 2: make sure to import urrlib.request, urllib.parse, urllib.error, ssl, and from bs4 import BeautifulSoup

#Step 3: Initialize the count variables and identify/count the paragraph tags 

import urllib.request 
import urllib.parse
import urllib.error 
import ssl 
from bs4 import BeautifulSoup

import collections #I am importing collections, as well as calling collections with the following code below because
#it is the only way I have found to run the code on VS Code. Otherwise, its not necessary
collections.Callable = collections.abc.Callable

count = 0 #initialize variables 
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve the paragraph tag
tags = soup('p')
#can also enter code print(len(tags)) as alternative to initializing
#and using count method below
for tag in tags:
    count += 1 #count the tags
print(count)

