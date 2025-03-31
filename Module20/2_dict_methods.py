# Задача 1. Склады
#
# У мебельного магазина есть два склада, на которых хранятся разные категории товаров по парам «название — количество»:

# small_storage = {
#     'гвозди': 5000,
#     'шурупы': 3040,
#     'саморезы': 2000
# }
#
# big_storage = {
#     'доски': 1000,
#     'балки': 150,
#     'рейки': 600
# }
#
# Магазин решил сократить аренду и скинуть все товары в большой склад (big_storage). После этого нас попросили
# реализовать поиск по товарам.
#
# Напишите программу, которая объединяет оба словаря в один (в big_storage), затем запрашивает у пользователя
# название товара и выводит на экран его количество. Если такого товара нет, то выводит об этом ошибку. Для
# получения значения используйте метод get.

small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}

big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}

big_storage.update(small_storage)

name_product = input('Введите название товара: ')

if big_storage.get(name_product):
    print(name_product, ':', big_storage.get(name_product))
else:
    print('Такого товара нет')

# Задача 2. Кризис фруктов
#
# Мы работаем в одной небольшой торговой компании, где все данные о продажах фруктов за год сохранены в словаре
# в виде пар «название фрукта — доход»:

# incomes = {
#     'apple': 5600.20,
#     'orange': 3500.45,
#     'banana': 5000.00,
#     'bergamot': 3700.56,
#     'durian': 5987.23,
#     'grapefruit': 300.40,
#     'peach': 10000.50,
#     'pear': 1020.00,
#     'persimmon': 310.00,
# }

# В компании наступил небольшой кризис, и нам поручено провести небольшой анализ дохода.
#
# Напишите программу, которая находит общий доход, затем выводит фрукт с минимальным доходом и удаляет его из
# словаря. Выведите итоговый словарь на экран.
#
# Результат работы программы:
#
# Общий доход за год составил 35419.34 рублей
#
# Самый маленький доход у grapefruit. Он составляет 300.4 рублей
#
# Итоговый словарь: {'apple': 5600.2, 'orange': 3500.45, 'banana': 5000.0, 'bergamot': 3700.56, 'durian': 5987.23,
#                    'peach': 10000.5, 'pear': 1020.0, 'persimmon': 310.0}

incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

print('Общий доход за год составил {0} рублей'.format(sum(incomes.values())))
min_income = min(incomes, key=incomes.get)
print('Самый маленький доход у {0}. Он составляет {1} рублей'.format(min_income, incomes[min_income]))
incomes.pop(min_income)
print('Итоговый словарь: {}'.format(incomes))

# Задача 3. Гистограмма частоты
#
# Лингвистам нужно собрать данные о частоте букв в тексте, исходя из этих данных будет строиться гистограмма частоты
# букв.
#
# Напишите программу, которая получает сам текст и считает, сколько раз в строке встречается каждый символ. На экран
# нужно вывести содержимое в виде таблицы, отсортированное по алфавиту, а также максимальное значение частоты.

text = input('Введите текст: ')
hist_freq = dict()

for let in text:
    if let in hist_freq:
        hist_freq[let] += 1
    else:
        hist_freq[let] = 1

for i_h in hist_freq.keys():
    print(i_h, ':', hist_freq[i_h])
print('Максимальная частота: {}'.format(min(hist_freq.values())))



