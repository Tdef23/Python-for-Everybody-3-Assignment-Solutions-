#Exercise 1: Write a function called chop that 
#takes a list and modifies it, removing the first 
#and last elements, and returns None. Then write a 
#function called middle that takes a list and 
#returns a new list that contains all but the first 
#and last elements.

def chop(x):
    del x[0]
    del x[-1]

def middle(x):
    n = x[1:]
    del n[-1]
    return n

j_list = [4, 8, 15]
j2_list = [16, 23, 42]

chopj_list = chop(j_list)
print(j_list)
print(chopj_list)

middlej2_list = middle(j2_list)
print(j2_list)
print(middlej2_list)