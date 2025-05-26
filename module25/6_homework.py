# Задача 1. Драка
# Что нужно сделать
# Вы работаете в команде разработчиков мобильной игры, и вам досталась такая часть от ТЗ заказчика:
#
# Есть два юнита, каждый из них называется «Воин». Каждому устанавливается здоровье в 100 очков. Они бьют друг друга в
# случайном порядке. Тот, кто бьёт, здоровье не теряет. У того, кого бьют, оно уменьшается на 20 очков от одного удара.
# После каждого удара надо выводить сообщение, какой юнит атаковал и сколько у противника осталось здоровья. Как только
# у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.
import random
from gc import garbage

from module24.homework import action


class Warrior:
    def __init__(self, name, health = 100):
        self.name = name
        self.health = health

    def attack(self, oppenent):
        oppenent.health -= 20
        print(f'{self.name} атакует! У {oppenent.name} осталось {oppenent.health} очков\n')

warrior1 = Warrior('Воин1')
warrior2 = Warrior('Воин2')

while warrior1.health > 0 and warrior2.health > 0:
    attacker = random.choice([warrior1, warrior2])
    defender = warrior1 if attacker == warrior2 else warrior2
    attacker.attack(defender)

if warrior1.health > warrior2.health:
    print(f'{warrior1.name} одержал победу')
else:
    print(f'{warrior2.name} одержал победу')

# Задача 2. Студенты
# Что нужно сделать
# Реализуйте модель с именем Student, содержащую поля: «ФИ», «Номер группы», «Успеваемость» (список из пяти элементов).
# Затем создайте список из десяти студентов (данные о студентах можете придумать свои или запросить их у пользователя)
# и отсортируйте его по возрастанию среднего балла. Выведите результат на экран.

class Student:
    def __init__(self, name, number_group, grades):
        self.name = name
        self.number_group = number_group
        self.grades = grades

    def get_mean_ball(self):
        return sum(self.grades) / len(self.grades)

    def info(self):
        print('Студент: {} \nГруппа: {} \nУспеваемость: {} \nСредний балл: {:.2f}\n'.format(
            self.name, self.number_group, self.grades, self.get_mean_ball()
        ))

students = []

students.append(Student("Иванов Иван Иванович", "101", [4, 5, 3, 4, 5]))
students.append(Student("Петрова Анна Сергеевна", "102", [3, 2, 4, 5, 4]))
students.append(Student("Сидоров Алексей Владимирович", "103", [5, 4, 4, 3, 5]))
students.append(Student("Кузнецова Наталья Викторовна", "101", [3, 3, 2, 4, 3]))
students.append(Student("Лебедев Сергей Алексеевич", "102", [4, 4, 5, 4, 4]))
students.append(Student("Морозова Ольга Павловна", "103", [5, 5, 5, 4, 5]))
students.append(Student("Федоров Николай Петрович", "100", [2, 3, 2, 3, 3]))
students.append(Student("Смирнова Елена Игоревна", "101", [4, 4, 4, 4, 4]))
students.append(Student("Васильева Анна Владимировна", "102", [3, 5, 4, 5, 4]))
students.append(Student("Дмитриев Константин Юрьевич", "103", [5, 5, 5, 2, 1]))

sorted_students = sorted(students, key=lambda student: student.get_mean_ball(), reverse=True)

for i_student in sorted_students:
    i_student.info()

# Задача 3. Круг
# Что нужно сделать
# На координатной плоскости рисуются круги, у каждого круга следующие параметры: координаты X и Y центра круга и
# значение R ― радиус круга. По умолчанию центр находится в (0, 0), а радиус равен 1.
#
# Реализуйте класс «Круг», который инициализируется по этим параметрам. Круг также может:
#
# Находить и возвращать свою площадь.
# Находить и возвращать свой периметр.
# Увеличиваться в K раз.
# Определять, пересекается ли он с другой окружностью.

import math

class Circle:

    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def info(self):
        print('x: {} \ny: {} \nradius: {}'.format(self.x, self.y, self.r))
        print('Площадь: {} \nПериметр: {}\n'.format(self.get_s(), self.get_p()))

    def get_s(self):
        # площадь круга
        return math.pi * self.r ** 2

    def get_p(self):
        # периметр круга
        return 2 * math.pi * self.r

    def change_circle(self, k):
        # увеличение круга
        self.r += k

    def has_cross(self, other_circle):
        # определяет, пересекается ли круг с другим кругом
        distance_between_centers = math.sqrt((self.x - other_circle.x) ** 2 + (self.y - other_circle.y) ** 2)
        return distance_between_centers < self.r + other_circle.r

circle1 = Circle()
circle2 = Circle(2, 2, 1)
circle1.info()
circle1.change_circle(2)
if circle1.has_cross(circle2):
    print('Круги пересекаются')
else:
    print('Круги не пересекаются')


# Задача 4. Отцы, матери и дети
# Что нужно сделать
# Реализуйте два класса: «Родитель» и «Ребёнок». У родителя есть:
#
# Имя.
# Возраст.
# Список детей.
# И он может:
#
# Сообщить информацию о себе.
# Успокоить ребёнка.
# Покормить ребёнка.
# У ребёнка есть:
#
# Имя.
# Возраст (должен быть меньше возраста родителя хотя бы на 16 лет).
# Состояние спокойствия.
# Состояние голода.
# Реализация состояний — на ваше усмотрение. Это может быть и простой «флаг», и словарь состояний, и что-нибудь ещё
# интереснее.

class Child:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.states = {
            'calm': False,  # не спокойный по умолчанию
            'hungry': True  # голодный по умолчанию
        }

    def get_info(self):
        print(f'Ребенок: {self.name}')
        print(f'Имя: {self.age}')
        if self.states['calm']:
            print('Ребенок спокойный')
        else:
            print('Ребенок не спокойный')

        if self.states['hungry']:
            print('Ребенок голодный')
        else:
            print('Ребенок не голодный')


class Parent:

    def __init__(self, name, age):
        if age < 16:
            raise ValueError('Возраст родителя должен быть больше 16 лет.')
        self.name = name
        self.age = age
        self.children = []

    def add_child(self, child):
        if self.age - child.age < 16:
            raise ValueError('Возраст ребенка должен быть меньше возраста родителя на 16 лет')
        self.children.append(child)

    def get_info(self):
        print('Имя - ', self.name)
        print('Возраст - ', self.age)
        print(f'Дети {', '.join([child.name for child in self.children])}')

    def feed_child(self, child):
        if child in self.children:
            child.states['hungry'] = False
            print(f'{self.name} покормил(а) ребенка {child.name}')
        else:
            print(f'{child.name} не является ребенком {self.name}')

    def calm_child(self, child):
        if child in self.children:
            child.states['calm'] = True
            print(f'{self.name} успокоил(а) ребенка {child.name}')
        else:
            print(f'{child.name} не является ребенком {self.name}')


parent = Parent('Оля', 25)

child1 = Child('Вася', 10)
child2 = Child('Петя', 4)

try:
    parent.add_child(child1)
except ValueError as e:
    print(e)

try:
    parent.add_child(child2)
except ValueError as e:
    print(e)

parent.get_info()

parent.feed_child(child2)

child2.get_info()

parent.calm_child(child2)

child2.get_info()


# Задача 5. Весёлая ферма —2
# Что нужно сделать
# Мы продолжаем писать игру «Весёлая ферма», и теперь необходимо её немного модернизировать. Всё-таки кому-то нужно
# собирать урожай, и для этого нам понадобится садовник, у которого есть:
#
# Имя.
# Грядка с растением, за которым он ухаживает (в нашем случае пока только грядка с картошкой).
# И он может:
#
# Ухаживать за грядкой.
# Собирать с неё урожай (количество картошки ― пустой список).
# Модернизируйте программу, используя новый класс «Садовник». На всякий случай даём описание картошки и грядки.
#
# У картошки есть её номер в грядке, а также стадия зрелости. Она может предоставлять информацию о своей зрелости и
# расти. Всего у картошки может быть четыре стадии зрелости.
#
# Грядка с картошкой содержит список картошки, которая на ней растёт, и может, собственно, взращивать всю эту картошку,
# а также предоставлять информацию о зрелости всей картошки на своей территории.
#
# Проверьте работу программы, создав грядку из пяти картошек и отдав эту грядку садовнику. Пусть поухаживает за грядкой
# и соберёт урожай (может быть, даже и не один).

class Potato:
    states = {0: 'отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, number):
        self.number = number
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def print_state(self):
        print('Картошка {} сейчас {}'.format(
            self.number, Potato.states[self.state]
        ))

    def is_ripe(self):
        if self.state == 3:
            return True
        return False


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([potato.is_ripe() for potato in self.potatoes]):
            print('Картошка еще не созрела')
            return False
        else:
            print('Картошка созрела')
            return True


class Gardener:
    def __init__(self, name, potato_garden):
        self.name = name
        self.garden = potato_garden
        self.harvest_count = []

    def get_info(self):
        print(f'Садовник: {self.name}')
        print(f'Собрано урожая: {sum(self.harvest_count)}')

    def take_care(self):
        self.garden.grow_all()

    def harvest(self):
        if self.garden.are_all_ripe():
            self.harvest_count.append(len(self.garden.potatoes))


garden = PotatoGarden(5)
gardener = Gardener('Иван', garden)

gardener.get_info()

for _ in range(3):
    gardener.take_care()
    gardener.harvest()

gardener.get_info()


# Задача 6. Магия
# Что нужно сделать
# Для одной игры необходимо реализовать механику магии, где при соединении двух элементов получается новый. У нас есть
# четыре базовых элемента: «Вода», «Воздух», «Огонь», «Земля». Из них как раз и получаются новые: «Шторм», «Пар», «Грязь»,
# «Молния», «Пыль», «Лава».
#
# Вот таблица преобразований:
#
# «Вода» + «Воздух» = «Шторм»
# «Вода» + «Огонь» = «Пар»
# «Вода» + «Земля» = «Грязь»
# «Воздух» + «Огонь» = «Молния»
# «Воздух» + «Земля» = «Пыль»
# «Огонь» + «Земля» = «Лава»
# Напишите программу, которая реализует все эти элементы. Каждый элемент необходимо организовать как отдельный класс.
# Если результат не определён, то возвращается None.
#
# Примечание: сложение объектов можно реализовывать через магический метод __add__, вот пример использования:
#
# class Example_1:
#     def __add__(self, other):
#         return Example_2()
#
# class Example_2:
#     answer = 'сложили два класса и вывели'
#
# a = Example_1()
# b = Example_2()
# c = a + b
# print(c.answer)
#
# Дополнительно: придумайте свой элемент (или элементы), а также реализуйте его взаимодействие с остальными элементами.

class Water:
    def __init__(self):
        self.name = 'Вода'

    def __add__(self, other):
        if other.name == 'Воздух':
            return Storm()
        elif other.name == 'Огонь':
            return Steam()
        elif other.name == 'Земля':
            return Dirt()
        else:
            return None

class Air:
    def __init__(self):
        self.name = 'Воздух'

    def __add__(self, other):
        if other.name == 'Вода':
            return Storm()
        elif other.name == 'Огонь':
            return Lightning()
        elif other.name == 'Земля':
            return Dust()
        else:
            return None


class Fire:
    def __init__(self):
        self.name = 'Огонь'

    def __add__(self, other):
        if other.name == 'Вода':
            return Steam()
        elif other.name == 'Воздух':
            return Lightning()
        elif other.name == 'Земля':
            return Lava()
        else:
             return None

class Land:
    def __init__(self):
        self.name = 'Земля'

    def __add__(self, other):
        if other.name == 'Вода':
            return Dirt()
        elif other.name == 'Воздух':
            return Dust()
        elif other.name == 'Огонь':
            return Lava()
        else:
            return None


class Storm:
    def __init__(self):
        self.name = 'Шторм'

class Steam:
    def __init__(self):
        self.name = 'Пар'

class Dirt:
    def __init__(self):
        self.name = 'Грязь'

class Lightning:
    def __init__(self):
        self.name = 'Молния'

class Dust:
    def __init__(self):
        self.name = 'Пыль'

class Lava:
    def __init__(self):
        self.name = 'Лава'


water = Water()
air = Air()
fire = Fire()
land = Land()

print(f'{water.name} + {air.name} = {(water + air).name}')
print(f'{water.name} + {fire.name} = {(water + fire).name}')
print(f'{water.name} + {land.name} = {(water + land).name}')
print(f'{air.name} + {fire.name} = {(air + fire).name}')
print(f'{air.name} + {land.name} = {(air + land).name}')
print(f'{fire.name} + {land.name} = {(fire + land).name}')


# Задача 7. Совместное проживание
# Что нужно сделать
# Чтобы понять, стоит ли ему жить с кем-то или всё же лучше остаться в гордом одиночестве, Артём решил провести довольно
# необычное исследование. Для этого он реализовал модель человека и модель дома.
#
# Человек может:
#
# Есть (+ сытость, − еда).
# Работать (− сытость, + деньги).
# Играть (− сытость).
# Ходить в магазин за едой (+ еда, − деньги).
# У человека есть имя, степень сытости (изначально 50) и дом.
#
# В доме есть холодильник с едой (изначально 50 еды) и тумбочка с деньгами (изначально 0 денег).
#
# Если сытость человека становится меньше нуля, то человек умирает.
#
# Логика действий человека определяется следующим образом:
#
# Генерируется число кубика от 1 до 6.
# Если сытость < 20, то поесть.
# Иначе, если еды в доме < 10, то сходить в магазин.
# Иначе, если денег в доме < 50, то работать.
# Иначе, если кубик равен 1, то работать.
# Иначе, если кубик равен 2, то поесть.
# Иначе играть.
# По такой логике эксперимента человеку надо прожить 365 дней.
#
# Реализуйте такую программу и создайте двух людей, живущих в одном доме. Проверьте работу программы несколько раз.

import random

class Person:
    def __init__(self, name, house):
        self.name = name
        self.fullness = 50
        self.house = house

    def eat(self):
        if self.house.eat > 0:
            self.fullness += 20
            self.house.eat -= 10
            print(f'{self.name} поел, сытость - {self.fullness}, еда в холодильнике - {self.house.eat}')
        else:
            print(f'{self.name} еды в холодильнике нет')

    def work(self):
        self.fullness -= 10
        self.house.money += 20
        print(f'{self.name} поработал. Сытость - {self.fullness}, деньги в тумбочке - {self.house.money}')

    def play(self):
        self.fullness -= 5
        print(f'{self.name} поиграл. Сытость - {self.fullness}')

    def shopping(self):
        if self.house.money > 0:
            self.house.eat += 30
            self.house.money -= 20
            print(f'{self.name} сходил в магазин. Еды в холодильнике - {self.house.eat}, денег в тумбочке - {self.house.money}')
        else:
            print(f'{self.name} не хватает денег для похода в магазин')

    def perform_action(self):
        if self.fullness < 20:
            self.eat()
        elif self.house.eat < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        else:
            cubic = random.randint(1, 6)
            if cubic == 1:
                self.work()
            elif cubic == 2:
                self.play()


class House:
    def __init__(self):
        self.eat = 50
        self.money = 0


def simulate_day(persons):
    for person in persons:
        if person.fullness <= 0:
            print(f'{person.name} умер')
            continue
        person.perform_action()


house = House()
person1 = Person('Петя', house)
person2 = Person('Маша', house)

for i in range(365):
    print(f'День номер {i+1}')
    simulate_day([person1, person2])
    print('-' * 30)
    print()

#
# Задача 8. Блек-джек
# Что нужно сделать

# Костя так и не смог завязать с азартными играми. Но перед тем как в очередной раз всё проиграть, он решил как
# следует подготовиться. И написать программу, на которой он будет тренироваться играть в блек-джек.
#
# Блек-джек также известен как 21. Суть игры проста: нужно или набрать ровно 21 очко, или набрать очков больше, чем
# в руках у дилера, но ни в коем случае не больше 21. Если игрок собирает больше 21, он «сгорает». В случае ничьей
# игрок и дилер остаются при своих.
#
# Карты имеют такие «ценовые» значения:
#
# от двойки до десятки — от 2 до 10 соответственно;
# у туза — 1 или 11 (11, пока общая сумма не больше 21, далее 1);
# у «картинок» (король, дама, валет) — 10.
# Напишите программу, которая вначале случайным образом выдаёт пользователю и компьютеру по две карты и затем
# запрашивает у пользователя действие: взять карту или остановиться. На экран должна выдаваться информация о руке
# пользователя. После того как игрок останавливается, выведите на экран победителя.
#
# Представление карты реализуйте с помощью класса.
#
# Дополнительно: сделайте так, чтобы карты не могли повторяться.
#
# Ваши классы в этой задаче могут выглядеть так:
#
# class Card:
#
#     # Карта, у которой есть значения
#     # — масть
#     # — ранг/принадлежность: 2, 3, 4, 5, 6, 7 и так далее
#
# class Deck:
#     # Колода создаёт у себя объекты карт
#
# class Player:
#     # Игрок, у которого есть имя и какие-то карты на руках

import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def value(self):
        if self.rank in ('J', 'Q', 'K'):
            return 10
        elif self.rank == 'A':
            return 11
        else:
            return int(self.rank)

    def __str__(self):
        return f'{self.suit} - {self.rank}'


class Desk:
    def __init__(self):
        self.cards = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = [str(n) for n in range(2, 11)] + ['J', 'Q', 'K', 'A']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
        random.shuffle(self.cards)


    def draw_card(self):
        return self.cards.pop() if self.cards else None




class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def hand_value(self):
        total = 0
        aces = 0
        for card in self.hand:
            total += card.value()
            if card.rank == 'A':
                aces += 1
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    def __str__(self):
        return f'{self.name} на руках карты {', '.join([str(card) for card in self.hand])}'


def determinate_winner(player, dealer):
    player_score = player.hand_value()
    dealer_score = dealer.hand_value()

    print(player)
    print(dealer)
    print(f"{player.name} : {player_score}, Дилер: {dealer_score}")

    if player_score > 21:
        print(f"{player.name} проиграл! Дилер выиграл!")
    elif dealer_score > 21:
        print(f"Дилер проиграл! {player.name} выиграл !")
    elif player_score > dealer_score:
        print(f"{player.name} выиграл!")
    elif player_score < dealer_score:
        print("Дилер выиграл!")
    else:
        print("Ничья!")


deck = Desk()
name = input('Введите имя игрока: ')
player = Player(name)
dealer = Player('Dealer')

for _ in range(2):
    player.add_card(deck.draw_card())
    dealer.add_card(deck.draw_card())

while True:
    print(player)
    action = int(input('Выберите действие, 1 - Взять карту, 2 - остановиться: '))
    if action == 1:
        player.add_card(deck.draw_card())
        if player.hand_value() > 21:
            break
    elif action == 2:
        break
    else:
        print('Выбрано некорректное действие!')

while dealer.hand_value() < 17:
    dealer.add_card(deck.draw_card())

determinate_winner(player, dealer)


# Задача 9. Крестики-нолики
# Что нужно сделать
# Напишите программу, которая реализует игру «Крестики-нолики». Да, это всё условие задачи.
#
# Ваши классы в этой задаче могут выглядеть так:
#
# class Cell:
#     #  Клетка, у которой есть значения
#     #   — занята она или нет
#     #   — номер клетки
#
# class Board:
#     #  Класс поля, который создаёт у себя экземпляры клетки
#
# class Player:
#     #  У игрока может быть
#     #   — имя
#     #   — на какую клетку ходит

class Cell:
    def __init__(self, num, state=False):
        self.num = num
        self.state = state
        self.symbol = ' '

    def occupy(self, symbol):
        if not self.state:
            self.state = True
            self.symbol = symbol
            return True
        return False


class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]

    def display(self):
        print('\n')
        for i in range(0, 9, 3):
            print(f'{self.cells[i].symbol} | {self.cells[i + 1].symbol} | {self.cells[i + 2].symbol}')
            if i < 6:
                print('-----------')
        print('\n')

    def is_full(self):
        return all(cell.state for cell in self.cells)

    def check_winner(self):
        for i in range(0, 9, 3):
            if self.cells[i].symbol == self.cells[i + 1].symbol == self.cells[i + 2].symbol != ' ':
                return self.cells[i].symbol

        for i in range(3):
            if self.cells[i].symbol == self.cells[i + 3].symbol == self.cells[i + 6].symbol != ' ':
                return self.cells[i].symbol

        if self.cells[0].symbol == self.cells[4].symbol == self.cells[8].symbol != ' ':
            return self.cells[0].symbol
        if self.cells[2].symbol == self.cells[4].symbol == self.cells[6].symbol != ' ':
            return self.cells[2].symbol

        return None


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        while True:
            try:
                num = int(input(f'{self.name}, выберите клетку (1-9): '))
                if 1 <= num <= 9:
                    if board.cells[num-1].occupy(self.symbol):
                        return
                    else:
                        print('Эта клетка уже занята.')
                else:
                    print('Введите число от 1 до 9')
            except ValueError:
                print('Пожалуйста, введите число!')


def play_game():
    board = Board()
    player1 = Player('Игрок1 (X)', 'x')
    player2 = Player('Игрок2 (O)', 'o')
    current_player = player1

    print("Добро пожаловать в игру Крестики-нолики!")
    print("Номера клеток:")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")

    while True:
        board.display()
        current_player.make_move(board)

        winner = board.check_winner()

        if winner:
            board.display()
            print(f'Поздравляем, {winner} победил!')
            break

        if board.is_full():
            print('Ничья!')
            break

        current_player = player2 if current_player == player1 else player1


play_game()





