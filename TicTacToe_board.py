from IPython.display import clear_output


def player_marker():
    marker = ' '
    while not (marker == 'X' or marker == 'O'):
        marker = input("(Player1) Please pick your marker - 'X' or 'O': ").upper()
    player_marker.player1 = marker
    if player_marker.player1 == 'X':
        player_marker.player2 = 'O'
    else:
        player_marker.player2 = 'X'
    print(f'Player1 is {player_marker.player1}, Player2 is {player_marker.player2}')
    return (player_marker.player1, player_marker.player2)

def reset_board():
    # clears board at the beginning of each game
    reset_board.board = [' '] * 10
    print('Welcome to TicTacToe!')
    return

def display_board():
    clear_output()
    print(' ' + reset_board.board[7] + ' ' + '|' + ' ' + reset_board.board[8] + ' ' + '|' + ' ' + reset_board.board[9])
    print('---|---|---')
    print(' ' + reset_board.board[4] + ' ' + '|' + ' ' + reset_board.board[5] + ' ' + '|' + ' ' + reset_board.board[6])
    print('---|---|---')
    print(' ' + reset_board.board[1] + ' ' + '|' + ' ' + reset_board.board[2] + ' ' + '|' + ' ' + reset_board.board[3])


def choose_number_player1():
    while True:
        try:
            player1_input = int(input('Player1, choose number: '))
            if player1_input not in range(1, 10):
                choose_number_player1()
            break
        except ValueError:
            print('Digits only!')
    while True:
        try:
            if not (reset_board.board[player1_input] == 'X' or reset_board.board[player1_input] == 'O'):
                reset_board.board.pop(player1_input)
                reset_board.board.insert(player1_input, player_marker.player1)
            else:
                print('This number is taken!')
                choose_number_player1()
            break
        except:
            break


def choose_number_player2():
    while True:
        try:
            player2_input = int(input('Player2, choose number: '))
            if player2_input not in range(1, 10):
                choose_number_player2()
            break
        except ValueError:
            print('Digits only!')
    while True:
        try:
            if not (reset_board.board[player2_input] == 'X' or reset_board.board[player2_input] == 'O'):
                reset_board.board.pop(player2_input)
                reset_board.board.insert(player2_input, player_marker.player2)
            else:
                print('This number is taken!')
                choose_number_player2()
            break
        except:
            break
