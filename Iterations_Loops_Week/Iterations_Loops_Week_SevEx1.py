count = 0
total = 0

while True:
    val = input('Enter number:')
    if val == 'done':
        break
    try:
        fval = float(val)
    except:
        print('Invalid Input')
        continue #allows us to track where the error occured in the event of a traceback
    #print(fval) allows to keep track of entered numbers
    count = count + 1
    total = total + fval

#print('All Done') keeps track of code process for debugging purposes
print(total, count, total/count)
