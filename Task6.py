# 6. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена
# составить не менее b километров. Программа должна принимать значения параметров a и b
# и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
a = int(input('Введите расстояние пробежки в киллометрах в день: '))
b = int(input('Введите результат расстояния пробежки, которого вы хотите добиться: '))
day = 1
day = a

print(f'1-й день:', day)


while a < b:
    a = (a * 0.1) + a
    print('{}-й день: {:.2f}'.format(day, a))
    day += 1
