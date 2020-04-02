from TicTacToe_board import *
from time import sleep


def check_if_someone_won():
    if ((reset_board.board[1] == 'X' and reset_board.board[2] == 'X' and reset_board.board[3] == 'X')
        or (reset_board.board[4] == 'X' and reset_board.board[5] == 'X' and reset_board.board[6] == 'X')
        or (reset_board.board[7] == 'X' and reset_board.board[8] == 'X' and reset_board.board[9] == 'X')
        or (reset_board.board[1] == 'X' and reset_board.board[4] == 'X' and reset_board.board[7] == 'X')
        or (reset_board.board[2] == 'X' and reset_board.board[5] == 'X' and reset_board.board[8] == 'X')
        or (reset_board.board[3] == 'X' and reset_board.board[6] == 'X' and reset_board.board[9] == 'X')
        or (reset_board.board[1] == 'X' and reset_board.board[5] == 'X' and reset_board.board[9] == 'X')
        or (reset_board.board[3] == 'X' and reset_board.board[5] == 'X' and reset_board.board[7] == 'X')) or \
            ((reset_board.board[1] == 'O' and reset_board.board[2] == 'O' and reset_board.board[3] == 'O')
             or (reset_board.board[4] == 'O' and reset_board.board[5] == 'O' and reset_board.board[6] == 'O')
             or (reset_board.board[7] == 'O' and reset_board.board[8] == 'O' and reset_board.board[9] == 'O')
             or (reset_board.board[1] == 'O' and reset_board.board[4] == 'O' and reset_board.board[7] == 'O')
             or (reset_board.board[2] == 'O' and reset_board.board[5] == 'O' and reset_board.board[8] == 'O')
             or (reset_board.board[3] == 'O' and reset_board.board[6] == 'O' and reset_board.board[9] == 'O')
             or (reset_board.board[1] == 'O' and reset_board.board[5] == 'O' and reset_board.board[9] == 'O')
             or (reset_board.board[3] == 'O' and reset_board.board[5] == 'O' and reset_board.board[7] == 'O')):
        print('You have won!')
        replay()
    else:
        pass


def check_if_stalemate():
    n = reset_board.board.count(' ')
    if n < 2:
        print('It\'s a stalemate!')
        replay()
    else:
        pass


def replay():
    answer = ''
    while not (answer == 'Y' or answer == 'N'):
        answer = input('Do you want to play again (Y/N)? ').upper()
    if answer == 'N':
        print('Thanks for the game! See you next time! :)')
        exit()
    elif answer == 'Y':
        print('Prepare...')
        sleep(2)
        TicTacToe()


def TicTacToe():
    # The game itself
    reset_board()
    player_marker()
    print(' ' + '7' + ' ' + '|' + ' ' + '8' + ' ' + '|' + ' ' + '9')
    print('---|---|---')
    print(' ' + '4' + ' ' + '|' + ' ' + '5' + ' ' + '|' + ' ' + '6')
    print('---|---|---')
    print(' ' + '1' + ' ' + '|' + ' ' + '2' + ' ' + '|' + ' ' + '3')
    while True:
        choose_number_player1()
        display_board()
        check_if_someone_won()
        check_if_stalemate()
        choose_number_player2()
        check_if_someone_won()
        display_board()

TicTacToe()
