# 1.	В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
b = []
for n in range(2, 10):
    count = 0
    for i in range(2, 100):# Делаем переменную- счетик и прогоняем по массиву чисел
         if i % n == 0:
            count += 1
    print(f' for {n} - {count}')
