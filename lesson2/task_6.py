# 6.	В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за
# 10 попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.
from random import randint
a = randint(1,100)
counter = 10
while counter > 0:
    b = int(input("Enter number:"))
    if b > a:
        print("Your number is bigger than hidden")
    elif b < a:
        print("Your number is less than hidden")
    else:
        print('You are right')
        break
    counter -=1
