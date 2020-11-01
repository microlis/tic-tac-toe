from random import randint


def print_board(board):
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')


def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Вы будете играть X или O: ')

    if marker == 'X':
        return 'X', 'O'
    if marker == 'O':
        return 'O', 'X'


def place_marker(board, marker, position):
    board[position] = marker


def check_board(board, position):
    return board[position] == ' '


def player_action(board, marker):
    while (True):
        position = 0
        while not (position in range(1, 10)):
            position = int(input('Выберите позицию (1-9): '))
            if position not in range(1, 10):
                print('Пожалуйста, выберите место с 1-9.')

        if check_board(board, position) == True:
            place_marker(board, marker, position)
            break
        else:
            print('Занято. Выберите другое.')


def win_check(board, marker):
    return (([marker] * 3 == [board[1]] + [board[4]] + [board[7]]) or
            ([marker] * 3 == [board[1]] + [board[2]] + [board[3]]) or
            ([marker] * 3 == [board[1]] + [board[5]] + [board[9]]) or
            ([marker] * 3 == [board[9]] + [board[6]] + [board[3]]) or
            ([marker] * 3 == [board[7]] + [board[8]] + [board[9]]) or
            ([marker] * 3 == [board[7]] + [board[5]] + [board[3]]) or
            ([marker] * 3 == [board[4]] + [board[5]] + [board[6]]) or
            ([marker] * 3 == [board[8]] + [board[5]] + [board[2]]))


def player_turn():
    return randint(1, 2)


def check_full_board(board):
    return ' ' not in board


while (True):
    board = ['#'] + [' '] * 9

    turn = player_turn()
    print(f'Игрок {turn} ходит первым!')

    if turn == 1:
        p1_marker, p2_marker = player_input()

    if turn == 2:
        p2_marker, p1_marker = player_input()

    while (True):
        if turn == 1:
            print_board(board)
            player_action(board, p1_marker)

            if win_check(board, p1_marker):
                print_board(board)
                print(f'Игрок {turn} выиграл!')
                break

            else:
                if check_full_board(board):
                    print_board(board)
                    print('Ничья!')
                    break
                else:
                    turn = 2

        if turn == 2:
            print_board(board)
            player_action(board, p2_marker)

            if win_check(board, p2_marker):
                print_board(board)
                print(f'Игрок {turn} выиграл!')
                break

            else:
                if check_full_board(board):
                    print_board(board)
                    print('Ничья!')
                    break
                else:
                    turn = 1
