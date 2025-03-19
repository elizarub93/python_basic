# Задача 1. Язык математики
a = 8
b = 10
c = 12
d = 18
res = ((-3 + a ** 2) * b - 2 ** 3) / (c - 2 * d)
print('Итог:', res)

# Задача 2. Финансовый отчёт
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))
num4 = int(input('Введите четвертое число: '))
num12 = num1 + num2
num34 = num3 + num4
res = num12 / num34
print('итог:', res)

# Задача 3. Следующее и предыдущее числа
num = int(input('Ведите число: '))
num_after = num + 1
num_before = num - 1
print('После числа', num, 'идет число', num_after)
print('До числа', num, 'идет число', num_before)

# Задача 4. Площадь треугольника
a1 = int(input('введите первый катет: '))
b1 = int(input('введите второй катет: '))
s = a1 * b1 / 2
print('Площадь треуголиника:', s)

# Задача 5. Часы
count_minutes = int(input('Введите количество минут: '))
hours = count_minutes // 60
minutes = count_minutes % 60
print(hours, 'часов', minutes, 'минут')

# Задача 6. Проверяем бухгалтера
n1 = int(input('Введиет первое число: '))
n2 = int(input('Введиет второе число: '))
res = (n1 % 100) + (n2 % 100)
print('Итог:', res)

# Задача 7. Режем число на части
number = int(input('Введите число: '))
n1 = number // 1000
n2 = number // 100 % 10
n3 = number % 100 // 10
n4 = number % 10
print(n1)
print(n2)
print(n3)
print(n4)

# Задача 8. Поменять местами: не всё так просто! (необязательная, повышенной сложности)
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(a, b)
ab = a + b
a = ab - a
b = ab - b
print(a, b)
