# Задача 1. Яблоки
apples = 41
boxes = 3
full_boxes = apples // boxes
print('Всего полных ящиков:', full_boxes)
rest_apples = apples % boxes
print('Осталось яблок:', rest_apples)

# Задача 2. Последняя цифра
number = int(input('Введите число: '))
print('Номер дома:', number % 10)
print('Номер квартиры:', number // 10)