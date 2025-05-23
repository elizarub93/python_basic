# Задача 1. Космические рейнджеры
# В далеком (а может и не очень) будущем на некоторой планете можно купить космический корабль за пол-кредита (CR).
# Один CR это 2200 чатлов. Причем чатлы неделимы и являются всегда целым числом. Напишите простую программу-конвертор
# валют. В программу вводится количество чатлов, а она сообщает сколько это CR и сколько кораблей можно купить
# на эту сумму.

chatle = int(input('Введите количество чатлов: '))
CR = chatle / 2200
ship = int(CR / 0.5)

print(f'Это {CR} CR')
print(f'Можно купить {ship} кораблей(я)')


# Задача 2. Компьютерное зрение
# Вы участвуете в разработке робота, который играет в шахматы на реальной, физической шахматной доске
# размером 0.8 х 0.8 метра. Робот смотрит камерой на доску и видит расположение фигур в вещественных
# числах с очень высокой точностью.
#
# Напишите программу, в которую вводятся вещественные координаты шахматной фигуры, а программа определяет
# в какой клетке доски находится эта фигура. Каждая клетка доски имеет размер 10х10 см и целочисленные координаты,
# состоящие из двух чисел. Например левая верхняя клетка имеет целые координаты (0, 0), справа от неё клетка
# (1, 0) а снизу (0, 1). Также обеспечьте контроль ввода: нельзя выходить за границы доски.
X = float(input('Введите координату X: '))
Y = float(input('Введите координату Y: '))

xSquare = int(X * 10)
ySquare = int(Y * 10)
print(f'Фигура находится в клетке: {xSquare} {ySquare}')

# Задача 3. Точность и аккуратность
# Робот из задачи “Компьютерное зрение” правильно определяет на какой клетке стоят фигуры. Но вот беда, часто по вине
# соперника-человека фигуры стоят на доске не ровно по центру клетки, а со смещением. Если во время игры такое смещение
# станет слишком велико, то станет непонятно в какой клетке стояла фигура. Чтобы избежать этой ситуации нужно чтобы
# робот поправлял фигуры на доске, выставляя их по центру клетки. Модифицируйте программу “Компьютерное зрение” так,
# чтобы она выдавала не только номера клетки, в которой находится фигура но и две вещественных поправки: на сколько
# нужно подвинуть фигуру по горизонтали и вертикали для того чтобы она оказалась по центру своей клетки.
print('Введите местоположение фигуры')
X = float(input('По горизонтали: '))
Y = float(input('По вертикали: '))

if 0 < X < 0.8 or 0 < Y < 0.8:
    xSquare = int(X * 10)
    ySquare = int(Y * 10)
    print(f'Фигура находится в клетке: {xSquare} {ySquare}')
    x_center = xSquare / 10 + 0.05
    y_center = ySquare / 10 + 0.05
    delta_x = round(x_center - X, 3)
    delta_y = round(y_center - Y, 3)
    print(f'Поправьте положение фигуры на ({delta_x}, {delta_y})')
else:
    print('Точки с такими координатами не существует')
