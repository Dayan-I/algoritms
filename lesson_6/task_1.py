from random import random
import sys
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
print(sys.getsizeof(a), sys.getsizeof(c), sys.getsizeof(d), sys.getsizeof(e))
# Размеры переменных для 64 рязрядной системы, python 3.9