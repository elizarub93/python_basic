# Задача 1. Электронная очередь
# Нам дали заказ написать программу для электронной очереди. У каждого человека в очереди есть номер: нулевой,
# первый, второй, третий и так далее. Каждый час очередь уменьшается на одного человека, то есть уходит сначала
# нулевой номер, затем первый, второй и так далее. Наша программа получает на вход одно число — количество людей
# в очереди — и выводит на экран историю обслуживания очереди: какие номера в какой час оставались.
people = int(input('Введите количество людей в очереди: '))

for hour in range(people + 1):
    print(f'Идет час: {hour}')
    for num in range(hour, people):
        print('Номер в очереди', num)
    print()

# Задача 2. Цифры больше пяти
# Пользователь вводит последовательность из N чисел. Напишите программу, которая подсчитывает общее
# количество цифр больше пяти во всей последовательности.

count = int(input('Введите количество чисел: '))
count_number = 0

for index in range(count):
    number = int(input(f'Введите {index} число: '))
    while number > 0:
        if number % 10 > 5:
            count_number += 1
        number //= 10
print('Количество цифр больше пяти равно:', count_number)

# Задача 3. Лестница чисел
# Пользователь вводит число N. Напишите программу, которая по этому числу выводит вот такую лестницу из чисел:

number = int(input('Введите число: '))

for row in range(number+1):
    for col in range(row, number+1):
        print(col, end=' ')
    print()
