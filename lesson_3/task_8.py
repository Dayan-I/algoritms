# 8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную
# матрицу.
from random import random

M = 5
N = 4
a = []
for i in range(N):
    b = []
    for j in range(M-1):

        b.append(int(input('Enter number: ')))

    b.append(sum(b))
    a.append(b)

for i in a:
    for j in i:
        print(j, end=' ')
    print()





