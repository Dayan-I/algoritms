# 9.	Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и
# сумму его цифр.
a, b, c = (input('Enter your number:')), (input('Enter your number:')),(input('Enter your number:'))
x = 0
for i in a,b,c:
    s = 0
    for n in i:
        s += int(n)
        if s > x:
            x = s

print(x)
