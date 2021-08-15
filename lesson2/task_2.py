# 2.	Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
try:
    a = input('Enter number:')
    even = 0
    uneven = 0
    for i in a:
        if int(i) % 2 == 0:
            even += 1
        else: uneven += 1
    print(even, uneven)
except (ValueError) as e: print('Input number')#Проверка на ошибку вводных данных
