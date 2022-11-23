h = int(input('Enter Hours:'))
r = float(input('Enter Rate:'))

if h > 40:
    extra_pay = (h - 40) * r * 1.5
    gross_pay = (40 * r) + extra_pay
else:
    gross_pay = h * r

print('Pay:', gross_pay)
