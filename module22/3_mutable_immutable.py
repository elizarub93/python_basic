# Задача 1. Ошибка
# В одном проекте на 10 000 строк кода произошла критическая ошибка. Хорошо, что старший разработчик быстро её нашёл
# и исправил. Он решил проверить, смогли бы вы её исправить, если бы его не было на месте. Поэтому он написал для
# вас код с аналогичной ошибкой:
#
# Суть кода в том, что у вас есть общий словарь из нескольких ключей, значения которых равны ранее объявленным
# переменным. Затем вызывается функция, которая должна изменять значения словаря, добавляя к значениям случайное
# число, в зависимости от типа данных. Но при этом меняются и ранее объявленные переменные. Исправьте эту ошибку
# и убедитесь, что nums_list, some_dict и uniq_nums не меняются.
#
# Подсказка. Для копирования объектов есть несколько способов:
#
# Встроенный метод copy. Пример для словаря.
# Встроенный в Python модуль copy и функции copy.copy() и copy.deepcopy().


import random


def change_dict(dct):
    num = random.randint(1, 100)
    for i_key, i_value in dct.items():
        if isinstance(i_value, list):
            i_value.append(num)
        if isinstance(i_value, dict):
            i_value[num] = i_key
        if isinstance(i_value, set):
            i_value.add(num)


nums_list = [1, 2, 3]
some_dict = {1: 'text', 2: 'another text'}
uniq_nums = {1, 2, 3}
common_dict = {1: nums_list.copy(), 2: some_dict.copy(), 3: uniq_nums.copy(), 4: (10, 20, 30)}

change_dict(common_dict)
print(common_dict)



# Задача 2. Непонятно!
# Друг никак не может понять эту тему с изменяемыми и неизменяемыми типами, ссылками, объектами и их id. Видя, как
# он мучается, вы решили помочь ему и объяснить эту тему наглядно.
#
# Пользователь вводит любой объект. Напишите программу, которая выводит на экран тип введённых данных, информацию
# о его изменяемости, а также id этого объекта.
#
# Помните, что через input можно получить только строку, что бы вы ни вводили. В данном случае ввод можно выполнить
# вручную, просто вписав нужный объект в переменную, без использования функции input.


data_input = {"a": 10, "b": 20}
print('Тип данных: {}'.format(type(data_input)))
if isinstance(data_input, dict) or isinstance(data_input, set) or isinstance(data_input, list):
    print('Изменяемый (mutable)')
else:
    print('Неизменяемый (immutable)')

print('id объекта: {}'.format(id(data_input)))