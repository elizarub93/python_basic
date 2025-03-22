# Задача 1. Генерация списка
# Что нужно сделать
# Дано целое число N. Напишите программу, которая формирует список из нечётных чисел от одного до N.
number = int(input('Введите число: '))
list_odd_number = []

for num in range(number + 1):
    if num % 2 != 0:
        list_odd_number.append(num)

print(f'список нечетных чисел: {list_odd_number}')

# Задача 2. Турнир
# Что нужно сделать
# Для соревнований по волейболу необходимо сформировать турнирнирную сетку для восьми человек на два дня. На
# первый день решили выбрать каждого второго из списка участников.
#
# Дан список из восьми имён: Артемий, Борис, Влад, Гоша, Дима, Евгений, Женя, Захар. Напишите программу,
# которая выводит элементы списка только с чётными индексами.

list_names = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
count_names = 8

first_day_names = []

for index in range(count_names):
    if index % 2 == 0:
        first_day_names.append(list_names[index])

print(f'Первый день: {first_day_names}')


# Задача 3. Клетки
# Что нужно сделать
# В научной лаборатории выводят и тестируют новые виды клеток. Есть список из N этих клеток, элементом которого
# является показатель эффективности, а индексом — ранг клетки. Учёные отбирают клетки по следующему принципу —
# если эффективность клетки меньше её ранга, то она не подходит.
#
# Напишите программу, которая выводит на экран элементы списка, значения которых меньше их индекса.

count_cells = int(input('Количество клеток: '))
efficiency_cells = []
wrong_cells = []

for index in range(count_cells):
    efficiency = int(input(f'Эффективность {index + 1} клетки: '))
    efficiency_cells.append(efficiency)

for index in range(count_cells):
    if index > efficiency_cells[index]:
        wrong_cells.append(efficiency_cells[index])

print('Неподходящие значения: ', end='')
for wrong in wrong_cells:
    print(wrong, end=' ')

# Задача 4. Видеокарты
# Что нужно сделать
# В базе магазина электроники есть список видеокарт компании NVIDIA разных поколений. Вместо полных названий
# хранятся только числа, которые обозначают модель и поколение видеокарты. Недавно компания выпустила новую
# линейку видеокарт. Самые старшие поколения разобрали за пару дней.
#
# Напишите программу, которая удаляет списка видеокарт наибольшие элементы.

count_videocart = int(input('Количество видеокарт: '))
list_videocart = []

# добавляем видеокарты в список
for index in range(count_videocart):
    videocart = int(input(f'{index + 1} Видеокарта:'))
    list_videocart.append(videocart)

# ищем максимум
max_videocart = list_videocart[0]
for videocart in list_videocart:
    if videocart > max_videocart:
        max_videocart = videocart

# удаляем максимум из списка
new_list_videocart = []
for videocart in list_videocart:
    if videocart != max_videocart:
        new_list_videocart.append(videocart)

print(f'Старый список видеокарт: {list_videocart}')
print(f'Новый список видеокарт: {new_list_videocart}')

# Задача 5. Кино
# Что нужно сделать
# Илья зашёл на любительский киносайт, на котором пользователи оставляют рецензии на фильмы. Их список:
# films = [‘Крепкий орешек’, ‘Назад в будущее’, ‘Таксист’, ‘Леон’, ‘Богемская рапсодия’, ‘Город грехов’, ‘Мементо’, ‘Отступники’, ‘Деревня’]
# Илья на сайте в первый раз. Он хочет зарегистрироваться и сразу добавить часть фильмов в список любимых, чтобы
# позже прочитать рецензии на них.
#
# Напишите программу, в которой пользователь вводит фильм. Если фильм есть в перечне, то добавляется в список любимых.
# Если фильма нет, то выводится ошибка. В конце выведите весь список любимых фильмов.

count_films = int(input('Сколько фильмов хотите добавить? '))
films = ['Крепкий орешек’', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
list_favorite_film = []

for _ in range(count_films):
    my_film = input('Введите название фильма: ')
    is_inlist = False
    for film in films:
        if film == my_film:
            is_inlist = True
    if is_inlist:
        list_favorite_film.append(my_film)
    else:
        print(f'Ошибка: фильма {my_film} у нас нет :(')

print('Ваш список любимых фильмов:', end='')
for film in list_favorite_film:
    print(film, end=' ')

# Задача 6. Анализ слова
# Что нужно сделать
# Напишите программу-анализатор слов, чтобы использовать её для тренировки нейросети и генерировать нужный текст.
#
# Напишите программу, которая считает количество уникальных букв во введённом пользователем слове. Уникальные буквы —
# это те, которые встречаются всего один раз.
word = input('Введите слово: ')
list_letters = list(word)
unique_letters = [ ]

for index in range(len(list_letters)):
    add_to_list = True
    for index_2 in range(len(list_letters)):
        if list_letters[index] == list_letters[index_2] and index != index_2:
            add_to_list = False
    if add_to_list:
        unique_letters.append(list_letters[index])

print(f'Количество уникальных букв: {len(unique_letters)}')

# Задача 7. Контейнеры
# Что нужно сделать
# Контейнеры на складе лежат в ряд в порядке невозрастания (меньше либо равно) массы в килограммах. На склад
# привезли ещё один контейнер, который нужно положить на определённое место.
#
# Напишите программу, которая получает на вход невозрастающую последовательность натуральных чисел. Они означают
# массу каждого контейнера в ряду. После этого вводится число X — масса нового контейнера. Программа выводит номер,
# под которым будет лежать новый контейнер. Если в ряде есть контейнеры с массой, как у нового, то его нужно
# положить после них.
# Обеспечьте контроль ввода: все числа не превышают 200.

count_containers = int(input('Количество контейнеров: '))
list_weights_containers = []

for _ in range(count_containers):
    weight = int(input('Введите вес контейнера: '))
    if weight > 200:
        print('Вес контейнера превышает 200')
        weight = int(input('Введите вес контейнера: '))
    list_weights_containers.append(weight)

another_container = int(input('Введите вес нового контейнера:'))
index_another_container = 0

for index in range(len(list_weights_containers)):
    if list_weights_containers[index] <= another_container:
        index_another_container = index + 1
        break

print(f'Номер, который получит новый контейнер: {index_another_container}')

# Задача 8. Бегущие цифры
# Что нужно сделать
# Напишите программу для маленького табло, в котором циклически повторяется один и тот же текст или числа.
# Например, как в метро, автобусах или трамваях.
#
# Даны список из N элементов и целое число K. Напишите программу, которая циклически сдвигает элементы списка
# вправо на K позиций. Используйте минимально возможное количество операций присваивания.
count_elem = int(input('Введите количество элементов в списке '))
list_elem = []
new_list_elem = []

for _ in range(count_elem):
    num = int(input('Введите число: '))
    list_elem.append(num)

shift = int(input('Сдвиг: '))
print(f'Изначальный список: {list_elem}')

for index in range(count_elem - shift, count_elem):
    new_list_elem.append(list_elem[index])

for index in range(count_elem - shift):
    new_list_elem.append(list_elem[index])

# Задача 9. Анализ слова 2
# Что нужно сделать
# Продолжите писать анализаторы для текста. Теперь необходимо реализовать код, с помощью которого можно определять
# палиндромы — слова, которые одинаково читаются слева направо и справа налево.

word = input('Введите слово: ')
list_word = list(word)
len_list_word= len(list_word)
reverse_list = []

for index in range(len_list_word):
    reverse_list.append(list_word[len_list_word - index - 1])

if reverse_list == list_word:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')

# Задача 10. Сортировка
# Что нужно сделать
# Дан список из N чисел. Напишите программу, которая сортирует элементы списка по возрастанию и выводит их на
# экран. Дополнительный список нельзя использовать.
#
# Также нельзя использовать готовые функции sorted/min/max и метод sort.
#
# Постарайтесь придумать и написать как можно более эффективный алгоритм сортировки.

list_num = [1, 4, -3, 0, 10]

print(f'Изначальный список: {list_num}')

for index1 in range(len(list_num)):
    for index2 in range(index1, len(list_num)):
        if list_num[index1] > list_num[index2]:
            list_num[index1], list_num[index2] = list_num[index2], list_num[index1]

print(f'Отсортированный список: {list_num}')







