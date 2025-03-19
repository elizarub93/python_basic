# Задача 1. Пропавшая переменная
client = 'Петя'
pet = 'Кот'
print(client)
print(' и ')
print(pet)

# Задача 2. Цвета
r = 'Red'
b = 'Blue'
g = 'Green'
print(r, b, g, r + b + g, b, g + b)

# Задача 3. Животные
first_animal = 'Заяц'
second_animal = 'Черепаха'
print(first_animal, 'спит,', second_animal, 'идет')

# Задача 4. Информация о пользователе
first_name = input('Введите имя: ')
second_name = input('Введите фамилию: ')
city = input('Введите город проживания: ')
print('Вас зовут ')
print(first_name)
print(second_name)
print('Вас зовут', first_name, second_name)
print('Вы живете в городе:', city)

# Задача 5. Вход в систему
first_name = input('Введите имя пользователя: ')
greeting = 'Привет,'
print(greeting, first_name)
print('К сожалению, у Вас нет доступа к системе.')
print('Пожалуйста, обратитесь к системному администратору.')

# Задача 6. Полёт
departure_city = input('Введите город вылета: ')
arrival_city = input('Введите город прилете: ')
print(departure_city, '-', arrival_city)

# Задача 7. Путь к файлу
user = input('Введите имя пользователя: ')
new_file = input('Введите имя файла: ')
path_file = 'C:/' + user + '/docs/folder/' + new_file + '.txt'
print(path_file)

# Задача 8. По желанию. Обмен значений двух переменных
a = input('Введите первое слово: ')
b = input('Введите второе слово: ')
print(a, b)
a, b = b, a
print(a, b)