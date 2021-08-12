#8.	Определить, является ли год, который ввел пользователем, високосным или не високосным.
a= int(input('Enter year:'))

if a % 4 == 0 and a % 100 != 0 or a% 400 == 0:
    print(True)
else: print(False)