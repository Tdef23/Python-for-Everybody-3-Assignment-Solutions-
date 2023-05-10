#Exercise 2: Change your socket program so that it counts the number of 
#characters it has received and stops displaying any text after it has 
#shown 3000 characters. The program should retrieve the entire document 
#and count the total number of characters and display the count of the 
#number of characters at the end of the document.

#Step 1: copy from Ex1.py
#Step 2: Start empty byte stream to store document, remove decode line after break
#Step 3: After break line, add line of code to ensure that data received is sent to received as bytes
#Step 4: Decode the received byte stream, then print received with the brackets showing only the first 3000 index characters 
#Step 5: Add a print line below to print the len of received

import socket

try:
    url = input("Enter URL: ")
    host = url.split("/")[2] 

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80)) 
    cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n' 
    cmd = cmd.encode() 
    mysock.send(cmd)

    received = b"" #empty byte stream
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        received += data
    
    received = received.decode()
    print(received[:3000]) 
    print(len(received))

    mysock.close()
except:
    print('URL is improperly formatted or nonexistent')
    


