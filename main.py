# task_1
print('task_1')

a = float(input('Введіть перше дійсне число: '))
b = float(input('Введіть друге дійсне число: '))
print()

if a > 6 and b > 6:
    print('Оба числа більші числа 6')
else:
    print('Оба числа не більші числа 6')

if a > 6 or b > 6:
    print('Хоча б одне з чисел більші числа 6')
else:
    print('Жодне з чисел не більше числа 6')

if (a > 6 and b <= 6) or (a <= 6 and b > 6):
    print('Тільки одне з чисел більше числа 6')
else:
    print('Числа не відповідають умові "Тільки одне з чисел більше числа 6"')


# task_2
print()
print('task_2')
print()

x = int(input('Введіть ціле число: '))

if abs(x) < 10:
    print('Модуль з цього числа менший 10')
else:
    print('Модуль з цього числа більший або рівний 10')


# task_3
print()
print('task_3')

X = int(input('Введіть ціле чотирицифрове число: '))
c = X // 1000
d = (X % 1000) // 100
print()

if c % 2 == 0:
    print('Перша цифра є парною')
else:
    print('Перша цифра не є парною')

if d % 2 == 0:
    print('Друга цифра є парною')
else:
    print('Друга цифра не є парною')