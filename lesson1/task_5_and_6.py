#5.	Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
a = ord('a')#Это наша отправная точка, чтобы знать номер первой буквы алфавита

b = int(input('Enter number of letter:'))#Это номер буквы которую надо найти
c = ord(input('Enter first letter:')) - a + 1#Это нижняя граница
d = ord(input('Enter second letter:')) - a + 1#Это верхняя граница
print(f'First letter position {c}, second letter psoition {d}, betweem them {d-c-1} letters)')
print(f'Yor letter is: {chr(b +a -1)}')