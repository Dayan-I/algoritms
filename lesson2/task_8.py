# 8.	Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество
# вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
a = input("Enter number:")
b = input("Enter number you want to count:")
counter = 0
for i in a:
    if b == i:
        counter +=1
print(f'Number {b} occurs in number {a} {counter} times.')
