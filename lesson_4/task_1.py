import cProfile
import random
def find_min1():
    a = [random.randint(-10, 10) for i in range(100000)]
    b = sorted(a, reverse=False)[0:2]# Встроенная сортировка
    print(b)
cProfile.run('find_min1()')

def find_min2():#Данная функция работает немного быстрее, скорее всего из за того что мы не сортируем массив, а просто проходим по нему два раза
    a = [random.randint(-10, 10) for i in range(100000)]
    b = 0
    c = []
    for i in a:
        if i < b:
            b = i
    c.append(b)#Добавили первый минимальный элемент
    a.remove(b)
    b = 0
    for i in a:
        if i < b:
            b = i
    c.append(b)#Добавили второй минимальный элемент

    print(c)

cProfile.run('find_min2()')