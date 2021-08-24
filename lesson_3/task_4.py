#4.	Определить, какое число в массиве встречается чаще всего.
import random
a = [random.randint(0, 10) for i in range(10)]
print(a)
d = {}
for i in a:
    n = 1 # Здесь не учитывем цифры которые всречаются 1 раз, тогда все цифры уникальны
    if a.count(i) >n:# Действуем с помощью спискового метода count
        n = a.count(i)
        d[i] = n #Добавляем в словарь число и сколько раз оно встречается

for k,v in d.items():
    print(f'Number {k} occurs {v} times')



