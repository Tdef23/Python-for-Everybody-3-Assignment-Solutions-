total = 0
count = 0
average = 0
while True:
    try:
        numbers = input('Enter a number: ')
        if numbers == 'done':
            print('Total: ',total)
            print('Count: ',count)
            print('Average: ',average)
            break
        num = float(numbers)
        total += num
        count += 1
        average = total / count
    except:
        print('Bad Input')
