#9.	Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
c = int(input('Enter third number:'))
m = a
if m < b:
    m = b
    if a < c:
        print(f'min {a}, middle {c}, max {b}')
    else:
        print(f'min {c}, middle {a}, max {b}')
elif m < c:
    m = c
    if a < b:
        print(f'min {a}, middle {b}, max {c}')
    else:
        print(f'min {b}, middle {a}, max {c}')
else:
    if b < c: print(f'min {b}, middle {c}, max {a}')
    else:
        print(f'min {c}, middle {b}, max {a}')
