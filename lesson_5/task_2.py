# 2.	Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# коллекция, элементы которой это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’,
# ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’,
# ‘E’].
import collections
number1 = list(''.join(input("Enter 1st number: ").split(' ')))
number2 = list(''.join(input("Enter 2nd number: ").split(' ')))

a = collections.OrderedDict()
hex_1 = {'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15}
for k, v in enumerate(number1, start=1):
    if v.isdigit():
        a[v] = int(v) * (16 ** (len(number1) - k))
    else:
        a[v] = hex_1[v] * (16 ** (len(number1) - k))

b = collections.OrderedDict()
for k, v in enumerate(number2, start=1):
    if v.isdigit():
        b[v] = int(v) * (16 ** (len(number2) - k))
    else:
        b[v] = hex_1[v] * (16 ** (len(number2) - k))

number1 = sum(a.values())
number2 = sum(b.values())
print(a)
print(b)
def summ(x,y):
    summ_1 = []
    if len(x) > len(y):
        n = 0
        for i in range(len(y)):
            z = (x.popitem()[1] + y.popitem()[1])
            if z > 15:
                summ_1.append(z % 16)
                n = z % 16
            else :
                summ_1.append(z // 16 +n)
        for k in x:
            summ_1.append(x.popitem()[0])
    else:
        n = 0
        for i in range(len(x)):
            z = (x.popitem()[1] + y.popitem()[1])
            if i == 0:
                summ_1.append(z % 16)
                n = z % 16
            else:
                summ_1.append(z // 16 +n)
        for k in y:
            summ_1.append(y.popitem()[0])
    summ_1.reverse()
    for i, v in enumerate(summ_1):
        if v in hex_1.values():
            summ_1[i] = list(hex_1.keys())[list(hex_1.values()).index(v)]

    print(summ_1)
summ(a,b)

