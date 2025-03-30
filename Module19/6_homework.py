# Задача 1. Меню ресторана
# Что нужно сделать
# Один ресторан заказал вам написать приложение, которое по одному клику отображало бы пользователю доступное
# меню в удобном виде. Для этого ресторан любезно предоставил свой сайт, откуда можно получить актуальную
# информацию о меню в виде идущих подряд названий.
#
# Напишите программу, которая выводит меню на экран. На вход подаётся строка из названий блюд, разделённых
# символом «;», а на выходе эти названия перечисляются через запятую и пробел.
#
# Пример:
# Доступное меню: утиное филе;фланк-стейк;банановый пирог;плов
# На данный момент в меню есть: утиное филе, фланк-стейк, банановый пирог, плов

menu = input('Доступное меню: ')
menu_list = menu.split(';')
print('На данный момент в меню есть: {}'.format(', '.join(menu_list)))

# Задача 2. Самое длинное слово
# Что нужно сделать
# Пользователь вводит строку, содержащую пробелы. Найдите в ней самое длинное слово, выведите это слово
# и его длину. Если таких слов несколько, выведите первое из них.
#
# Пример 1:
# Введите строку: я есть строка
# Самое длинное слово: строка
# Длина этого слова: 6
#
# Пример 2:
# Введите строку: а б
# Самое длинное слово: а
# Длина этого слова: 1
#
# Пример 3:
# Введите строку: б
# Самое длинное слово: б
# Длина этого слова: 1

text = input('Введите строку: ')
text_list = text.split(' ')

long_word = text_list[0]

for word in text_list:
    if len(word) > len(long_word):
        long_word = word

print('Самое длинное слово: {}'.format(long_word))
print('Длина этого слова: {}'.format(len(long_word)))

# Задача 3. Файлы
# Что нужно сделать
# В одной IT-компании существует негласный закон об именовании текстовых документов:
#
# Название файла не должно начинаться на один из специальных символов: @, №, $, %, ^, &, *, ().
# Файл заканчивается расширением .txt или .docx.
# Напишите программу, которая получает на вход полное название файла и проверяет его по этим правилам.
#
# Пример 1:
# Название файла: @example.txt
#
# Ошибка: название начинается на один из специальных символов.
#
# Пример 2:
# Название файла: example.ttx
#
# Ошибка: неверное расширение файла. Ожидалось .txt или .docx.
#
# Пример 3:
# Название файла: example.txt
#
# Файл назван верно.

name_file = input('Название файла: ')
special_char_list = '@, №, $, %, ^, &, *, ()'.split(', ')
is_special = False

for char in special_char_list:
    if name_file.startswith(char):
        is_special = True
        break

if is_special:
    print('Ошибка: название начинается на один из специальных символов.')
elif not (name_file.endswith('.txt') or name_file.endswith('.docx')):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Файл назван верно.')

# Задача 4. Заглавные буквы
# Что нужно сделать
# Пользователь вводит строку. Напишите программу, которая изменяет регистр символов в этой строке так, чтобы первая
# буква каждого слова была прописной, а остальные буквы — строчными.
#
# Пример:
# Введите строку: Кажется, я забыл выключить утюг.
# Результат: Кажется, Я Забыл Выключить Утюг.

text = input('Введите строку: ')
print('Результат: {}'.format(text.title()))

# Задача 5. Пароль
# Что нужно сделать
# При регистрации на сайте, помимо логина, нужно придумать надёжный пароль. Этот пароль должен состоять минимум
# из восьми символов, в нём должна быть хотя бы одна прописная буква и хотя бы три цифры. Тогда он будет считаться
# надёжным.
#
# Напишите программу, которая запрашивает пароль у пользователя до тех пор, пока пароль не окажется надёжным.
# Используется латиница.
#
# Пример:
# Придумайте пароль: qwerty
# Пароль ненадёжный. Попробуйте ещё раз.
# Придумайте пароль: qwerty12
# Пароль ненадёжный. Попробуйте ещё раз.
# Придумайте пароль: qwerty123
# Пароль ненадёжный. Попробуйте ещё раз.
# Придумайте пароль: qWErty123
# Это надёжный пароль!

while True:
    password = input('Придумайте пароль:')
    count_digit = 0
    count_upper = 0

    for char in password:
        if char.isdigit():
            count_digit += 1
        elif char.isupper():
            count_upper += 1
    if len(password) < 8 or count_digit < 3 or count_upper < 1:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        print('Это надёжный пароль!')
        break

# Задача 6. Сжатие
# Что нужно сделать
# С увеличением объёма данных возникла потребность в сжатии этих данных без потери важной информации. Для этого
# было придумано кодирование, которое осуществляется следующим образом:
#
# s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот
# символ и количество его повторений в этой позиции строки.
#
# Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную
# последовательность на экран. Кодирование должно учитывать регистр символов.
#
# Пример:
# Введите строку: aaAAbbсaaaA
#
# Закодированная строка: a2A2b2с1a3A1

text = input('Введите строку: ')
list_char = []
count_list_char = []
prev_char = ''

for char in text:
    if char == prev_char:
        count_list_char[-1] += 1
    else:
        list_char.append(char)
        count_list_char.append(1)
        prev_char = char

new_text = ''
for i_c in range(len(list_char)):
    new_text = new_text + ''.join([list_char[i_c], str(count_list_char[i_c])])

print('Закодированная строка: {}'.format(new_text))

# Задача 7. IP-адрес 2
# Что нужно сделать
# При написании клиент-серверного приложения часто приходится работать с IP-адресами. Как вы уже знаете, IP-адрес
# состоит из четырёх целых чисел в диапазоне от 0 до 255, разделённых точками.
#
# Пользователь вводит строку. Напишите программу, которая определяет, является ли заданная строка правильным IP-адресом.
# Обеспечьте контроль ввода, где предусматривается ввод целых чисел от 0 до 255, а также точки между ними.
#
# Пример 1:
# Введите IP: 128.16.35.a4
# a4 — это не целое число.
#
# Пример 2:
# Введите IP: 240.127.56.340
# 340 превышает 255.
#
# Пример 3:
# Введите IP: 34.56.42,5
# Адрес — это четыре числа, разделённые точками.
#
# Пример 4:
# Введите IP: 128.0.0.255
# IP-адрес корректен.

def chech_ip(ip_address):
    ip_address_list = ip_address.split('.')
    for num in ip_address_list:
        if num.isnumeric():
            if int(num) > 255:
                return '{} превышает 255.'.format(num)
        else:
            if num.isalnum():
                return '{} — это не целое число.'.format(num)
            else:
                return 'Адрес — это четыре числа, разделённые точками.'
    return 'IP-адрес корректен.'

ip_address = input('Введите IP: ')
ip_address_list = ip_address.split('.')

print(chech_ip(ip_address))


# Задача 8. Бегущая строка
# Что нужно сделать
# В одной из практических работ вы писали для табло программу, которая циклически сдвигает элементы списка чисел
# вправо на K позиций. В этот раз вы работаете с двумя строками. Нужно проверить, равна ли на самом деле одна
# другой. Возможно, одна из них просто немного сдвинута.
#
# Пользователь вводит две строки. Напишите программу, которая определяет, можно ли получить первую строку из
# второй циклическим сдвигом.
#
# Опционально: если получить можно, то выведите значение этого сдвига.
#
# Пример 1:
# Первая строка: abcd
# Вторая строка: cdab
# Первая строка получается из второй со сдвигом 2.
#
# Пример 2:
# Первая строка: abcd
# Вторая строка: cdba
# Первую строку нельзя получить из второй с помощью циклического сдвига.


def shift_str(text, shift):
    new_text = ''
    for i_c in range(len(text)):
        new_text += text[(i_c + shift) % len(text)]
    return new_text

first_text = input('Первая строка: ')
second_text = input('Вторая строка: ')
shift = 0

for i_s in range(1, len(first_text)):
    if shift_str(second_text, i_s) == first_text:
        shift = i_s
        break

if shift > 0:
    print('Первая строка получается из второй со сдвигом {}.'.format(shift))
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')

#
# Задача 9. Сообщение
# Что нужно сделать
# Вашему другу надоело общаться простыми сообщениями и он решил делать это необычным способом — он переворачивает
# каждое слово в тексте, при этом не трогая знаки препинания.
#
# Пользователь вводит текст, состоящий из слов и знаков препинания. Напишите программу, которая переворачивает
# (записывает в обратном порядке) все слова текста, оставив знаки препинания без изменений. Словом в тексте
# считается последовательность символов из прописных и строчных букв кириллицы.
#
# Пример 1:
# Сообщение: Это задание очень! простое.
# Новое сообщение: отЭ еинадаз ьнечо! еотсорп.
#
# Пример 2:
# Сообщение: Хотя ,. возм:ожно и нет.
# Новое сообщение: ятоХ ,. мзов:онжо и тен.
def reverse_word(word):
    if word.isalpha():
        return word[::-1]
    temp_word, new_word = '', ''
    for char in word:
        if char.isalpha():
            temp_word += char
        else:
            new_word += temp_word[::-1] + char
            temp_word = ''
    new_word += temp_word[::-1]
    return new_word

message = input('Сообщение: ')
list_message = message.split()
new_list_message = [reverse_word(word) for word in list_message]

new_message = ' '.join(new_list_message)

print('Новое сообщение: {}'.format(new_message))

# Задача 10. Истина
# Что нужно сделать
# К вам попал зашифрованный текст, означающий большую истину для многих программистов на Python. Напишите программу,
# которая реализует алгоритм дешифровки этого текста. Расшифруйте текст с помощью своей программы, а затем найдите
# его в интернете.

def step1(text_list):
    output_list = []
    shift = 3
    for word in text_list:
        correct_word  = ''.join([word[-shift % len(word):], word[:-shift % len(word)]])
        output_list.append(correct_word)
        if correct_word in '/':
            shift += 1
    return output_list


text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf'\
       ' jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp'\
       ' djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme '\
       'wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv '\
       'Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc '\
       'bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ'\
       ' ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb '\
       'cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'

text_list = text.split()

print(step1(text_list))





