#	Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import random
M = 3
N = 3
a = []
for i in range(N):
    b = []
    for j in range(M):
        b.append(int(random() * 10))

    a.append(b)
c = []
d = []
for i in range(M):
    s = 10#Мы знаем верхнюю границу
    for j in range(N):
        if a[j][i] < s:

            s = a[j][i]
            c.append(s)#доавбляем в список
    d.append(c[-1])#и достаем последний член списка
e = max(d)

for i in a:
    for j in i:
        print(j, end=' ')
    print()
print(c)
print(d)
print(e)
