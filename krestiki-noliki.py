# print("Добро пожаловать в игру \"Крестики-Нолики\"!")
pole_headline = ['  0 1 2']
poles = ['0', '1', '2']
pole = [['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]
winner = 0
player = 1

def print_table(table):
    global winner
    print(*pole_headline)
    for i in range(len(table)):
        print(i, *table[i])
    for i in range(len(pole)):
        if any([pole[i][0]
                == pole[i][1]
                == pole[i][2] == 'X',
                pole[0][i]
                == pole[1][i]
                == pole[2][i] == 'X',
                pole[0][0]
                == pole[1][1]
                == pole[2][2] == 'X',
               pole[0][2]
               == pole[1][1]
               == pole[2][0] == 'X']):
            winner = 1
        elif any([pole[i][0]
                == pole[i][1]
                == pole[i][2] == '0',
                pole[0][i]
                == pole[1][i]
                == pole[2][i] == '0',
                pole[0][0]
                == pole[1][1]
                == pole[2][2] == '0',
                  pole[0][2]
                  == pole[1][1]
                  == pole[2][0] == '0']):
            winner = 2
        else:
            pass

print_table(pole)

def request_data():
    global player
    while True:
        a, b = input(f'Игрок {player}, введите номер строки и номер столбца через пробел').split()
        if any([a not in poles,
               b not in poles]):
            print('Введите корректные значения')
            continue
        a, b = int(a), int(b)
        if pole[a][b] != '-':
            print("Поле уже занято")
            continue
        if player == 1:
            pole[a][b] = 'X'
            player = 2
        else:
            pole[a][b] = '0'
            player = 1
        print_table(pole)
        break

while winner == 0:
    request_data()

print(f"Игрок {winner}, поздравляем с победой!")


