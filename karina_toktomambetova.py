import random
from random import choice


def initial_capital():
    with open('settings.ini') as file:
        for line in file:
            line = line.strip()
            if line.startswith('MY_MONEY'):
                key, value = line.split('=')
                return int(value)
    return 0

def game():
    capital = initial_capital()
    numbers = list(range(1, 31))

    while True:
        print(f'Начальный капитал: {capital}')
        cash_rate = int(input('Сделайте ставку: '))
        if cash_rate > capital:
            print('Сумма ставки превышает Ваш капитал')
            continue

        number = int(input('Выберите число от 1 до 30: '))
        if number not in numbers:
            print('Неверное число!')
            continue

        winning_number = random.choice(numbers)
        print(f'Выигрышное число: {winning_number}')

        if number == winning_number:
            capital += cash_rate * 2
            print(f'Сумма выигрыша: {cash_rate * 2}')
        else:
            capital -= cash_rate
            print('Вы проиграли!')

        answer = input('Хотите сыграть еще? \nда/нет: ')
        if answer == 'нет':
            break

    if cash_rate > capital or cash_rate < capital:
        print(f'Текущая сумма на счету: {capital}')
    else:
        print(f'У Вас не осталось денег')
