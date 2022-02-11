print("Добро пожаловать в игру \"Крестики-Нолики\"!")

def game():

    while True:
        pole = [['-', '-', '-'],
                ['-', '-', '-'],
                ['-', '-', '-']]
        game_result = 0
        player = 1
        def print_table(table):
            nonlocal game_result
            pole_headline = ['  0 1 2']
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
                    game_result = 1
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
                    game_result = 2
                elif all(['-' not in pole[0],
                          '-' not in pole[1],
                          '-' not in pole[2]]):
                    game_result = 3
                else:
                    pass

        print_table(pole)

        while game_result == 0:
            a = input(f'Игрок {player}, введите номер строки')
            if a not in ['0', '1', '2']:
                print('Введите корректные значения')
                continue
            b = input(f'Игрок {player}, введите номер столбца')
            if b not in ['0', '1', '2']:
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

        if game_result != 3:
            print(f"Игрок {game_result}, поздравляем с победой!")
        else:
            print("Игра закончена, ничья!")

        while True:
            yn = input("Повторить еще? Y/N")
            if yn != 'Y' and yn != 'N':
                print("Не понял команды")
                continue
            else:
                break

        if yn == 'N':
            print("До свидания!")
            break
        elif yn == "Y":
            continue

game()






