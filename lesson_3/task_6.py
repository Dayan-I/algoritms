# 6.	В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами
# минимальный и максимальный элементы в сумму не включать.
import random
a = [random.randint(-10, 10) for i in range(10)]
c = max(a)
d = min(a)
b = sum([i for i in a if c > i >d])

print(a)
print(b)
