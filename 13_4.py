# Задача 1. Среднее арифметическое
# Программа получает от пользователя два числа — a и b. Реализуйте функцию, которая принимает на вход числа a и b,
# считает и выводит в консоль среднее арифметическое всех чисел из отрезка [a; b]. Обеспечьте контроль ввода:
# не забывайте, что а всегда должно быть меньше, чем b.

def segmentMean(a, b):
    summ = 0
    count = 0
    for number in range(a, b + 1):
        summ += number
        count += 1
    print(f'Среднее: {summ / count}')
a = int(input('Введите левую границу: '))
b = int(input('Введите правую границу: '))

if b > a:
    segmentMean(a, b)
else:
    print('Границы введены некорректно.')

# Задача 2. Почта 2
# На почте немного поменялись правила: теперь в почтовом извещении нужно указывать фамилию, имя, страну проживания,
# город, улицу, номер дома и номер квартиры.
# Реализуйте функцию, которая получает все эти данные и выводит на экран. В программе вызовите функцию три раза с
# разными значениями аргументов.
# Подсказка: семь аргументов.

def printInfo(firstName, name, country, city, street, houseNumber, flatNumber):
    print(f'Фамилия: {firstName}')
    print(f'Имя: {name}')
    print(f'Страна: {country}')
    print(f'Город: {city}')
    print(f'Улица: {street}')
    print(f'Номер дома: {houseNumber}')
    print(f'Номер квартиры: {flatNumber}')

firstName = input('Введите фамилию: ')
name = input('Введите имя: ')
country = input('Введите страну: ')
city = input('Введите город: ')
street = input('Введите улицу: ')
houseNumber = int(input('Введите номер дома: '))
flatNumber = int(input('Введите номер квартиры: '))
printInfo(firstName, name, country, city, street, houseNumber, flatNumber)

# Задача 3. GPS-навигатор 2.0
# Нам поручили усовершенствовать GPS-навигатор, добавив в него новую фишку. Теперь пользователь может не только
# смотреть расстояние от себя до объекта, но и задавать в навигаторе две произвольные точки, после чего на экран
# ему выводится расстояние между ними. Для этого пользователь вводит четыре действительных числа x1, y1, x2, y2 —
# это как раз координаты этих двух точек.
#
# Напишите программу, где у пользователя спрашивается, чего он хочет — найти расстояние от себя до точки или найти
# расстояние между двумя произвольными точками, после чего запрашиваются необходимые координаты точек и выводится
# ответ на экран.
import math
def myDistance(x, y):
    distance = math.sqrt(x ** 2 + y ** 2)
    print(f'Расстояние: {distance}')

def betweenDistance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(f'Расстояние: {distance}')

answer = int(input('1 - найти расстояние от себя до точки; 2 - от точки до точки: '))

if answer == 1:
    x = float(input('Введите икс: '))
    y = float(input('Введите игрек: '))
    myDistance(x, y)
elif answer == 2:
    x1 = float(input('Введите икс первой точки: '))
    y1 = float(input('Введите игрек первой точки: '))
    x2 = float(input('Введите икс второй точки: '))
    y2 = float(input('Введите игрек второй точки: '))
    betweenDistance(x1, y1, x2, y2)
else:
    print('Введено неверное значение.')

