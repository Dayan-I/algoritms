#3.	По введенным пользователем координатам двух точек вывести уравнение прямой вида
#y = kx + b, проходящей через эти точки.
a, b = int(input('Enter coordinate x1:')), int(input('Enter coordinate y1:'))
c, d = int(input('Enter coordinate x2:')), int(input('Enter coordinate y2:'))

k = (d-b)/(c-a)# коэффициент к можно выразить через уравнения y1 = kx1 + b и y2 = kx2 + b
m = b - k*a# b = y2 - kx2 =>> y1=kx1+y2-kx2 ==>> k = (y1-y2)/(x1-x2)
m1 = d - k*c# коэффициент b находится простым подставлением
print(k, m, m1)
