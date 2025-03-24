# Задача 1. Гласные буквы
# Что нужно сделать
# Команде лингвистов понравилось качество ваших программ и они решили заказать у вас функцию для анализатора
# текста, которая создавала бы список гласных букв текста и заодно считала бы их количество.
#
# Напишите программу, которая запрашивает у пользователя текст и генерирует список из гласных букв этого текста
# (сама строка вводится на русском языке). Выведите в консоль список и его длину.
#
# Пример:
# Введите текст: Нужно отнести кольцо в Мордор!
#
# Список гласных букв: ['у', 'о', 'о', 'е', 'и', 'о', 'о', 'о', 'о']
# Длина списка: 9

def is_vowel(letter):
    if letter in ['a', 'е', 'ё', 'и', 'у', 'о', 'ы', 'э', 'я', 'ю']:
        return True
    else:
        return False

text = input('Введите текст: ')
list_vowels = []
count_vowels = 0

for letter in text:
    if is_vowel(letter):
        list_vowels.append(letter)
        count_vowels += 1

print(f'Список гласных букв: {list_vowels}')
print(f'Длина списка: {count_vowels}')

# Задача 2. Генерация
# Что нужно сделать
# Пользователь вводит целое число N. Напишите программу, которая генерирует список из N чисел. На чётных местах в
# нём стоят единицы, а на нечётных — числа, равные остатку от деления своего номера на 5.
#
# Пример:
#
# Введите длину списка: 10
#
# Результат: [1, 1, 1, 3, 1, 0, 1, 2, 1, 4]

length_list = int(input('Введите длину списка: '))
list_num = [(1 if index % 2 == 0 else index % 5 for index in range(length_list))]
print(f'Результат: {list_num}')

# Задача 3. Случайные соревнования
# Что нужно сделать
# Мы хотим протестировать работу электронной таблицы для участников некоторых соревнований. Есть два списка
# (то есть две команды), по 20 участников в каждом. В этих списках хранятся очки каждого участника (вещественные
# числа с двумя знаками после точки, например, 4.03). Участник одной команды соревнуется с участником другой
# команды под таким же номером. То есть первый соревнуется с первым, второй — со вторым и так далее.
#
# Напишите программу, которая генерирует два списка участников (по 20 элементов) из случайных вещественных
# чисел (от 5 до 10). Для этого найдите подходящую функцию из модуля random. Далее сгенерируйте третий список,
# в котором окажутся только победители из каждой пары.
#
# Пример:
# Первая команда: [7.86, 6.76, 9.97, 9.08, 5.45, 6.9, 8.65, 5.17, 8.17, 5.06, 7.56, 7.1, 7.18, 8.25, 5.53, 7.95, 8.91, 7.11, 8.29, 9.52]
# Вторая команда: [7.13, 5.7, 8.89, 5.36, 5.62, 9.46, 5.82, 8.67, 8.41, 7.0, 5.31, 7.8, 9.93, 7.76, 7.4, 8.26, 7.94, 5.71, 7.89, 7.77]
# Победители тура: [7.86, 6.76, 9.97, 9.08, 5.62, 9.46, 8.65, 8.67, 8.41, 7.0, 7.56, 7.8, 9.93, 8.25, 7.4, 8.26, 8.91, 7.11, 8.29, 9.52]

import random
first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
winners = [ (first_team[i_winner] if first_team[i_winner] > second_team[i_winner]
             else second_team[i_winner])
            for i_winner in range(20)]

print(f'Первая команда: {first_team}')
print(f'Вторая команда: {second_team}')
print(f'Победители тура: {winners}')

# Задача 4. Тренируемся со срезами
# Что нужно сделать
# Дана строка, в которой хранятся первые семь букв английского алфавита.
#
# alphabet = 'abcdefg'
#
# Напишите программу, которая выводит на экран десять следующих результатов:
#
# Копию строки.
# Элементы строки в обратном порядке.
# Каждый второй элемент строки (включая самый первый).
# Каждый второй элемент строки после первого.
# Все элементы до второго.
# Все элементы, начиная с конца, до предпоследнего.
# Все элементы в диапазоне индексов от 3 до 4 (не включая 4).
# Последние три элемента строки.
# Все элементы в диапазоне индексов от 3 до 4.
# То же, что и в предыдущем пункте, но в обратном порядке.
# Для получения и вывода результатов используйте только команду print и срезы.

alphabet = 'abcdefg'
print(alphabet[:])
print(alphabet[::-1])
print(alphabet[::2])
print(alphabet[1::2])
print(alphabet[:1])
print(alphabet[7:5:-1])
print(alphabet[3:4])
print(alphabet[:3:-1])
print(alphabet[3:5])
print(alphabet[4:2:-1])

# Задача 5. Разворот
# Что нужно сделать
# На вход в программу подаётся строка, в которой буква h встречается как минимум два раза. Реализуйте код, который
# разворачивает последовательность символов, заключённую между первым и последним появлением буквы h, в
# противоположном порядке.

text = input('Введите строку: ')
text = text[:text.index('h'):-1]
text = text[text.index('h') + 1:]
print(f'Развёрнутая последовательность между первым и последним h: {text}')

# Задача 6. Сжатие списка
# Что нужно сделать
# Дан список из N целых случайных чисел (число от 0 до 2). Напишите программу, которая выполняет «сжатие списка» —
# переставляет все нулевые элементы в конец массива. При этом все ненулевые элементы располагаются в начале
# массива в том же порядке. Затем все нули из списка удаляются.
#
# Пример:
# Количество чисел в списке: 10
# Список до сжатия: [0, 2, 1, 0, 0, 0, 1, 0, 2, 0]
# Список после сжатия: [2, 1, 1, 2]

count_num = int(input('Количество чисел в списке: '))
list_num = [random.randint(0,2) for _ in range(count_num)]

print(f'Список до сжатия: {list_num}')

for i_num in range(count_num):
    if list_num[i_num] == 0:
        list_num.remove(0)
        list_num.append(0)
list_num = list_num[:list_num.index(0)]

print(f'Список после сжатия: {list_num}')

# Задача 7. Двумерный список
# Что нужно сделать
# Как мы говорили ранее, в программировании часто приходится писать код, исходя из результата, который требует
# заказчик. В этот раз заказчику нужно получить такой двумерный список:
#
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
#
# Напишите программу, которая генерирует и выводит на экран такой список. Используйте только list comprehensions.

list_num = [[random.randint(0, 20) for _ in range(3)] for _ in range(4)]
print(list_num)

# Задача 8. Развлечение
# Что нужно сделать
# N палочек выставили в один ряд, пронумеровав их слева направо числами от 1 до N. Затем по этому ряду бросили
# K камней, при этом камень i сбил все палки с номерами от L_i до R_i включительно. Определите, какие палки
# остались стоять на месте.
#
# Напишите программу, которая получает на вход количество палок N и количество бросков K. Далее идёт K пар
# чисел Left_i, Right_i, при этом 1 ≤ Left_i ≤ Right_i ≤ N.
#
# Программа должна вывести последовательность из N символов, где  символ j есть I, если палка j осталась
# стоять, и “.”, если палка j была сбита.

count_sticks = int(input('Количество палок: '))
count_shot = int(input('Количество бросков: '))
list_sticks = [1 for _ in range(count_sticks) ]

for i_s in range(count_shot):
    print(f'Бросок {i_s + 1}')
    begin = int(input('Сбиты палки с номера '))
    end = int(input('по номер '))
    list_sticks[begin - 1: end] = [0 for _ in range(end - begin + 1)]

print('Результат: ', end='')
for stick in list_sticks:
    if stick == 0:
        print('.', end='')
    elif stick == 1:
        print('|', end='')


# Задача 9. Список списков
# Что нужно сделать
# Дан такой (уже многомерный!) список:
#
# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
#
# Напишите код, который «раскрывает» все вложенные списки, то есть оставляет только внешний список. Для решения
# используйте только list comprehensions.
#
# Ответ: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

new_list = [nice_list[i_l][i_l2][i_l3] for i_l in range(len(nice_list))
            for i_l2 in range(len(nice_list[i_l]))
            for i_l3 in range(len(nice_list[i_l][i_l2]))]
print(new_list)

# Задача 10. Шифр Цезаря
# Что нужно сделать
# Юлий Цезарь использовал свой способ шифрования текста. Каждая буква заменялась на следующую по алфавиту через
# K позиций по кругу. Если K = 3, то в слове на основе русского алфавита, которое мы хотим зашифровать, буква
# «А» станет буквой «Г», «Б» станет «Д» и так далее.
#
# Пользователь вводит сообщение, а также значение сдвига. Напишите программу, которая зашифрует это сообщение при
# помощи шифра Цезаря.

alphabet = [chr(i) for i in range(ord('а'), ord('я') + 1)]

text = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))
new_text = []

for letter in text:
    if letter in alphabet:
        i_letter = (alphabet.index(letter) + shift) % len(alphabet)
        new_text += alphabet[i_letter]
    else:
        new_text += letter

print('Зашифрованное сообщение: ', end='')

for letter in new_text:
    print(letter, end='')
