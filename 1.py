from xml.etree.ElementPath import prepare_parent


def annuity(percent, period):
    t = (1 + percent) ** period
    return  percent * t / (t - 1)

def print_info(num_period, summa, percent):
    print(f'\nПериод: {num_period}')
    print(f'Остаток долга на начало периода: {summa:.2f}')
    print(f'Выплачено процентов: {summa_credit * percent:.2f}')
    payment = annuity_summa - summa_credit * percent
    print(f'Выплачено тела кредита: {payment:.2f}')
    return summa - payment


summa_credit = float(input('Введите сумму кредита: '))
period = int(input('На сколько лет выдан? '))
percent = float(input('Сколько процентов годовых?')) / 100

annuity_summa = annuity(percent, period) * summa_credit

for p in range(1, 4):
    summa_credit = print_info(p, summa_credit, percent)

print(f'\nОстаток долга: {summa_credit:.2f}')
print('=' * 20)

n2 = int(input('На сколько лет продлевается договор? '))
i2 = float(input('Увеличение ставки до: ')) / 100

period = n2 + period - 3

annuity_summa = annuity(i2, period) * summa_credit

for p in range(1, period+1):
    summa_credit = print_info(p, summa_credit, i2)

print(f'\nОстаток долга: {summa_credit:.2f}')