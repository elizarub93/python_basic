# Задача 1. Квадраты чисел
# Напишите программу, которая выводит квадраты чисел от 0 до 10. Для этого используйте цикл for и функцию range.

for number in range(11):
    print(number ** 2)

# Задача 2. Кукушка
# Напишите программу, которая имитировала бы часы с кукушкой. В начале работы она спрашивает, который час, а затем
# нужное количество раз пишет “Ку-ку!”.
hours = int(input('Который час? '))

for hour in range(hours):
    print('Ку-ку!')


# Задача 3. Любовь с первой цифры (цикл for)
# Перепишите программу из прошлого модуля, используя цикл for.
#
# Паша очень любит математику. Настолько сильно, что у него по всей комнате висят всякие таблицы умножения,
# сложения, какие-то графики, формулы. И теперь он захотел распечатать таблицу степеней двойки, у них как раз
# началась новая тема по информатике.
#
# Используя цикл for, выведите на экран для числа 2 его степени от 0 до 20.

for degree in range(21):
    print(2, '**', degree, '=', 2 ** degree)