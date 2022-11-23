total = 0
count = 0
largest = None
smallest = None
while True:
    try:
        numbers = input('Enter a number: ')
        if numbers == 'done':
            print('Total:',total)
            print('Count:',count)
            print('Maximum:', largest)
            print('Minimum:', smallest)
            break
        num = float(numbers)
        total += num
        count += 1
        if smallest is None or num <= smallest:
            smallest = num
        elif largest is None or num >= largest:
            largest = num
    except:
        print('Bad Input')


#Online Lesson alt exercise

#5.2 Write a program that repeatedly prompts a user for integer numbers until
#the user enters 'done'. Once 'done' is entered, print out the largest and
#smallest of the numbers. If the user enters anything other than a valid number
#catch it with a try/except and put out an appropriate message and ignore the
#number. Enter 7, 2, bob, 10, and 4 and match the output below.
largest = None
smallest = None

while True:
    try:
        num = input('Enter number:')
        if num == 'done':
            print('Maximum is', largest)
            print('Minimum is', smallest)
            break
        n = int(num)
        if largest is None or n > largest:
            largest = n
        elif smallest is None or n < smallest:
            smallest = n
    except:
        print('Invalid input')
