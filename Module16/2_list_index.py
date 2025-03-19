# Задача 1. Гугл
# Программисты постоянно гуглят ошибки и ищут уже готовый код, который можно использовать для своей программы,
# чтобы не изобретать велосипед. Андрей поступил также и нашёл для своего проекта код, который должен находить
# минимальное и максимальное числа в списке. Вот этот код:

nums_list = []
N = int(input('Кол-во чисел в списке: '))

for _ in range(N):
    num = int(input('Очередное число: '))
    nums_list.append(num)

maximum = nums_list[0]
minimum = nums_list[0]

for i in nums_list:
    if maximum < i:
        maximum = i
    if minimum > i:
        minimum = i

print('Максимальное число в списке:', maximum)
print('Минимальное число в списке:', minimum)

# Задача 2. Кратность
# Пользователь вводит список из N чисел и число K. Напишите код, выводящий на экран сумму индексов элементов
# списка, которые кратны K.

N = int(input('Кол-во чисел в списке: '))
N_list = []

for index in range(N):
    num = int(input(f'Введите {index + 1} число: '))
    N_list.append(num)

k = int(input('\nВведите делитель: '))
sum_index = 0

print()
for index in range(N):
    if N_list[index] % k == 0:
        print(f'Индекс числа {N_list[index]}: {index}')
        sum_index += index

print(f'Сумма индексов: {sum_index}')


# Задача 3. Собачьи бега
# В собачьих бегах участвует N собак, у каждой из них есть определённое количество очков за сезон. На огромном
# табло выводятся очки каждой собаки. Однако при выводе был обнаружен баг: собаки с наибольшим и наименьшим
# количеством очков поменялись местами! Нужно это исправить.
#
# Дан список очков из N собак. Напишите программу, которая меняет местами наибольший и наименьший элементы в списке.

count_dogs = int(input('Введите кол-во собак: '))
rating_list = []

for index in range(count_dogs):
    rating = int(input(f'Ведите рейтинг собаки номер {index + 1}: '))
    rating_list.append(rating)
# rating_list = [13, 34, 65, 25, 75]

minimum = rating_list[0]
maximum = rating_list[0]

index_minimum = 0
index_maximum = 0

for index in range(count_dogs):
    if rating_list[index] > maximum:
        maximum = rating_list[index]
        index_maximum = index
    if rating_list[index] < minimum:
        minimum = rating_list[index]
        index_minimum = index

rating_list[index_minimum], rating_list[index_maximum] = maximum, minimum

print(f'Итоговый лист: {rating_list}')
