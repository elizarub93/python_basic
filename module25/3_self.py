# Задача 1. Машина 2
#
# Модернизируйте класс Toyota из прошлого урока. Атрибуты остаются такими же:
#
# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
#
#
# Добавьте два метода класса:
#
# Отображение информации об объекте класса.
# Метод, который позволяет устанавливать текущую скорость машины.
# Проверьте работу этих методов.

class Toyota:
    color = 'red'
    price = 1000000
    max_speed = 200
    current_speed = 0

    def print_info(self):
        print(
            'Цвет машины: {} \nЦена машины: {}\nМаксимальная скорость машины: {}\nТекущая скорость машины: {}\n'.format(
                self.color, self.price, self.max_speed, self.current_speed
            )
        )

    def set_current_speed(self, speed):
        self.current_speed = speed

car1 = Toyota()
car1.print_info()
car1.set_current_speed(100)
car1.print_info()


# Задача 2. Семья
#
# Реализуйте класс «Семья», который состоит из атрибутов «Имя», Деньги» и «Наличие дома» и объекты которого могут
# выполнять следующие действия:
#
# Отобразить информацию о себе.
# Заработать денег (подаётся число, которое прибавляется к текущему значению денег).
# Купить дом (подаётся стоимость дома и необязательный аргумент «Скидка»). Вывести соответствующее сообщение об
# успешной/неуспешной покупке дома.
# Создайте как минимум один экземпляр класса и проверьте работу методов.

class Family:
    name = 'Common name'
    money = 100000
    has_house = False

    def info(self):
        print(
            'Фамилия: {} \nКоличество денег: {} \nНаличие дома:{} \n'.format(
                self.name, self.money, self.has_house
            )
        )

    def earned_money(self, money):
        self.money += money
        print('Заработано: {}\nОбщее количество денег: {} \n'.format(
            money, self.money)
        )

    def buy_house(self, price, discount=0):
        price -= price * discount / 100
        if self.money >= price:
            self.money -= price
            self.has_house = True
            print('Теперь у вас есть дом! Остаток на счете: {}\n'.format(self.money))
        else:
            print('Недостаточно денег для покупки дома.\n')

family = Family()
family.info()

print('Заработаем немного денег')
family.earned_money(100000)
family.info()

print('Попробуем купить дом')
family.buy_house(1000000)

if not family.has_house:
    print('Заработаем еще денег')
    family.earned_money(900000)
    print('И попробуем еще раз купить дом')
    family.buy_house(1000000, 5)

family.info()




