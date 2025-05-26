# Задача 1. Машина 3
#
# Вам предстоит снова немного видоизменить класс Toyota из прошлого урока. На всякий случай вот описание класса.
#
# Четыре атрибута:
#
# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
# Два метода:
#
# Отображение информации об объекте класса.
# Метод, который позволяет устанавливать текущую скорость машины.
# Теперь все четыре атрибута должны инициализироваться при создании экземпляра класса (то есть передаваться в init).
# Реализуйте такое изменение класса.

class Toyota:
    def __init__(self, color, price, max_speed, current_speed):
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.current_speed = current_speed


    def print_info(self):
        print(
            'Цвет машины: {} \nЦена машины: {}\nМаксимальная скорость машины: {}\nТекущая скорость машины: {}\n'.format(
                self.color, self.price, self.max_speed, self.current_speed
            )
        )

    def set_current_speed(self, speed):
        self.current_speed = speed

car1 = Toyota('red', 1000000, 200, 0)
car1.print_info()
car1.set_current_speed(100)
car1.print_info()


# Задача 2. Координаты точки
#
# Объект «Точка» на плоскости имеет координаты X и Y. При создании новой точки могут передаваться пользовательские
# значения координат, по умолчанию x = 0, y = 0.
#
# Реализуйте класс, который будет представлять эту точку, и напишите метод, который предоставляет информацию о ней.
# Также внутри класса пропишите счётчик, который будет отвечать за количество созданных точек.
#
# Подсказка: счётчик можно объявить внутри самого класса и увеличивать его в методе __init__.

class Point:
    count_point = 0

    def __init__(self, x=0, y=0):
        Point.count_point += 1
        self.x = x
        self.y = y

    def info(self):
        print('x: {}\ny: {}'.format(self.x, self.y))
        print(f'количество созданных точек: {self.count_point}\n')

point1 = Point(1, 1)
point1.info()

point2 = Point()
point2.info()

point3 = Point(2, 1)
point3.info()


# Задача 3. Весёлая ферма
#
# Для игры «Весёлая ферма» необходимо прописать два класса: класс «Картошка» и класс «Грядка картошки».
#
# У картошки есть её номер в грядке, а также стадия зрелости. Она может предоставлять информацию о своей зрелости и
# расти. Всего у картошки может быть четыре стадии зрелости.
#
# Грядка с картошкой содержит список картошки, которая на ней растёт, и может, собственно, взращивать всю эту картошку,
# а также предоставлять информацию о зрелости всей картошки на своей территории.
#
# Реализуйте оба класса и проверьте их работу: создайте экземпляр грядки из пяти картошек и три раза взрастите грядку.

class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зелёная', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def print_state(self):
        print('Картошка {} сейчас {}'.format(
            self.index, Potato.states[self.state]
        ))

    def is_ripe(self):
        if self.state == 3:
            return True
        return False


class PotatoGarden:
    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count+1)]

    def grow_all(self):
        print('Картошка прорастает')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка ещё не созрела!\n')
        else:
            print('Вся картошка созрела. Можно собирать!\n')


potatoes = PotatoGarden(5)
potatoes.are_all_ripe()

for _ in range(3):
    potatoes.grow_all()
    potatoes.are_all_ripe()
