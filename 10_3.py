# Задача 1. Python!
# Напишите программу, которая выводит в отдельную строчку каждый символ фразы “Python!”.

for symbol in 'Python!':
    print(symbol)


# Ваня экспериментирует с различного рода компьютерными вирусами, которые портят жизнь людям. На просторах Интернета
# он нашёл код довольно необычного вируса, который “поворачивает” весь текст в документе и повторяет каждый символ 3 раза.

text = input('Введите текст: ')

for symbol in text:
    print(symbol * 3)


# Задача 3.
# Мы входим в команду разработки нового текстового редактора и нам поручили разработать для него подсчёт нужного
# символа в тексте, а именно - буквы Ы. Причём отдельно с верхним регистром и отдельно с нижним.
#
# Напишите программу, которая считает количество больших и количество маленьких букв Ы в тексте и выводит ответ на экран.

text = input('Введите текст: ')
countBig = 0
countSmall = 0

for symbol in text:
    if symbol == 'Ы':
        countBig += 1
    elif symbol == 'ы':
        countSmall += 1

print('Больших букв Ы:', countBig)
print('Маленьких букв Ы:', countSmall)

