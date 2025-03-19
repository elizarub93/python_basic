# Задача 1. Вода
# Одна бутылка воды «КлирВотер» от производителя «ВодЗавод» в разных магазинах стоит по-разному.
#
# Напишите программу, которая три раза вызывает функцию aboutWater, передаёт в неё один аргумент — цену на воду и
# выводит на экран название воды, производителя и цену.
from curses.ascii import isprint


def aboutWater(price):
    print('Название: КлирВотер')
    print('Производитель: ВодЗавод')
    print(f'Цена: {price}')

aboutWater(25)
aboutWater(30)
aboutWater(27)

# Задача 2. Вот это объёмы 2
# Андрей продолжает писать курсовую работу по физике, и теперь ему нужно находить не только объём планеты, но и её
# площадь.
# Напишите программу, которая на вход получает от пользователя радиус планеты (вещественное число) и вызывает функции
# sphereArea и sphereVolume. Реализуйте эти функции: первая считает и выводит на экран площадь сферы, вторая —
# объём шара.
import math

def sphereArea(radius):
    print(f'Площадь сферы: {4 * math.pi * radius ** 2}')

def sphereVolume(radius):
    print(f'Объем шара: {4 / 3 * math.pi * radius ** 3}')

radius = float(input('введите радиус: '))
sphereArea(radius)
sphereVolume(radius)

# Задача 3. Простые числа
# Пользователь вводит число N — количество чисел в последовательности. Напишите программу, которая проверяет, сколько
# из этих чисел являются простыми. Для проверки простоты числа реализуйте функцию isPrime.

def isPrime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

countNumber = int(input('Введите количество чисел в последовательности: '))
countPrime = 0
for _ in range(countNumber):
    number = int(input('Введите число: '))
    if isPrime(number):
        countPrime += 1
print(f'Кол-во простых чисел: {countPrime}')