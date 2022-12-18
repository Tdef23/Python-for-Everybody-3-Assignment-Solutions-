#Exercise 6: Rewrite the program that prompts the user 
#for a list of numbers and prints out the maximum and 
#minimum of the numbers at the end when the user enters 
#"done". Write the program to store the numbers the user 
#enters in a list and use the max() and min() functions 
#to compute the maximum and minimum numbers after the loop 
#completes. 

#Enter a number: 6
#Enter a number: 2
#Enter a number: 9
#Enter a number: 3
#Enter a number: 5
#Enter a number: done
#Maximum: 9.0
#Minimum: 2.0 

new_list = []
while(True):
    num = input('Enter a number:')
    if num == 'done': 
        print('Enter a number:', num)       #records entry of "done"
        break
    try:
        float(num)
    except:
        print('Invalid Entry')              #guardian to make sure only a number is entered
        quit()
    print('Enter a number:', num)           #records number entered as mentioned in the instructions above
    new_list.append(num)                    #adds numbers to the list
    
print('Maximum:', float(max(new_list)))     #exits the loop and prints results
print('Minimum:', float(min(new_list)))