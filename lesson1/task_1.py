#1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
a = int(input('Enter your number:'))
b = 0
c = 1
for i in str(a): #Решение подоходит для любых чисел, а не только трехзначных
    b += int(i)
    c *= int(i)
print(b,c)