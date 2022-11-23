#Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and
#create a function called computepay which takes two parameters (hours and rate).
#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0

hr = float(input('Enter Hours:'))
rt = float(input('Enter Rate:'))

def computepay(hr, rt):
    if hr > 40:
        pay = (40 * rt) + ((hr - 40) * (1.5 * rt))
    else:
        pay = hr * rt
    return pay

pay = computepay(hr, rt)

print('Pay:', pay)
