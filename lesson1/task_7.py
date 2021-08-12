a = int(input('Enter first side:'))
b = int(input('Enter second side:'))
c = int(input('Enter third side:'))
d = max(a,b,c)

if not a+b <d or a+c<d or b+c<d:
    if (a == b and a !=c) or (a == c and a !=b) or (b == c and b !=a):
        print('Равнобедренный треугольник')
    elif a == c == b:
        print('Равносторонний треуголник')
    else:print('Разносторонний треугольник')


else: print("Невозможно составить треугольник из этих отрезков")