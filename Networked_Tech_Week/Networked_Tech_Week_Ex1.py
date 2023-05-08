#Exercise 1: Change the socket program socket1.py
#to prompt the user for the URL so it can read
#any web page. You can use split('/') to break
#the URL into its component parts so you can
#extract the host name for the socket connect 
#call. Add error checking using try and except
#to handle the condition where the user enters
#an improperly formatted or non-existent URL.

#test with https://www.py4e.com/code3/socket1.py

#Step 1: copy socket1.py code

import socket

try:
    url = input("Enter URL: ") #step 2: generate url input and test to find host by commenting out code below and doing print(url.split("/"))
    host = url.split("/")[2] #data.pr4e.org is the host, make host = code to generate it, uncomment everything below

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80)) #change host url to host from above
    cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n' #change to GET for generic url and split/concatenate 
    cmd = cmd.encode() #add cmd line to encode
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

    mysock.close()
except:
    print('URL is improperly formatted or nonexistent')