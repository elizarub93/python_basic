# Задача 1. Имена
# В базе данных одной компании есть баг (или, может быть, фича): если ввести туда имя сотрудника меньше чем из трёх
# букв, то база сломается и упадёт. Как компания принимает на работу людей, например, с китайскими именами, непонятно.
#
# Дан файл people.txt, в котором построчно хранится N имён пользователей.
#
# Напишите программу, которая берёт количество символов в каждой строке файла и в качестве ответа выводит общую сумму.
# Если в какой-либо строке меньше трёх символов (не считая литерала \n), то вызывается ошибка, и программа завершается.
from operator import truediv
from re import findall

try:
    people = open('people.txt', 'r', encoding='utf-8')
    sum_char = 0
    num_str = 0

    for name in people:
        num_str += 1
        count_name = len(name)
        if name.endswith('\n'):
            count_name -= 1
        if count_name < 3:
            raise BaseException('Имя в строке {} содержит меньше трех букв'.format(num_str))
        sum_char += count_name
finally:
    people.close()

print('Полное количество букв', sum_char)


# Задача 2. Логирование
# Возможно, вы замечали, что некоторые программы не просто выдают ошибку и закрываются, но и записывают эту ошибку в
# файл. Таким образом проще сформировать отчёт об ошибках, а значит, программисту будет проще их исправить. Это
# называется логированием ошибок.
#
# Дан файл words.txt, в котором построчно записаны слова. Необходимо определить количество слов, из которых можно
# получить палиндром (привет предыдущим модулям). Если в строке встречается число, то программа выдаёт ошибку
# ValueError и записывает эту ошибку в файл errors.log


def is_polindrom(text):
    return text == text[::-1]

words = open('words.txt', 'r', encoding='utf-8')
errors = open('errors.log', 'w')
count_polindrom = 0
num_str = 0

for word in words:
    try:
        num_str += 1
        word = word.rstrip()
        if word.isalpha():
            count_polindrom += is_polindrom(word)
        else:
            raise ValueError
    except ValueError:
        errors.write('В строке {} содержится число \n'.format(num_str))

words.close()
errors.close()

print('Количество полиндромов:', count_polindrom)






