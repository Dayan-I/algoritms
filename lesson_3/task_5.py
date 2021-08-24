#5.	В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве.
import random
a = [random.randint(-10, 10) for i in range(10)]
print(a)
b = -1
for i in a:
    if i < 0 and b == -1:
        b = a.index(i)
    elif i < 0 and i > a[b]:
        b = a.index(i)

print(a[b], b)