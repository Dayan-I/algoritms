# 1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных
# числа) для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и
# вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.
companies = {}
n = int(input('Enter numbers of companies'))
a = 0
for i in range(n):
    name = input("Enter name of company: ")
    first, second, third, fourth = int(input("Enter 1st quarter")), int(input("Enter 2nd quarter")), int(input("Enter 3rd quarter")),int(input("Enter 4th quarter"))
    companies[name] = first, second, third, fourth
    a += sum(companies[name])

avr = a / n

for k in companies:
    if sum(companies[k]) > avr:
        print(f'Revenue of company {k} is higher than average')
    else:
        print(f'Revenue of company {k} is less than average')
