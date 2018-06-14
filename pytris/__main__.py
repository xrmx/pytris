import sys

from .lib import init_board, win, move, EndGame


def main(args=None):
    board = init_board()
    one = input("player one")
    two = input("player two")
    marks = {
        'x': one,
        'o': two
    }
    turn = 'x'
    while True:
        pos = input('{}, fai la tua mossa'.format(marks[turn]))
        x, y = pos.split(' ')
        if not move(board, int(x), int(y), turn):
            continue
        try:
            end, winner = win(board)
            if end:
                print('{} ha vinto!'.format(winner))
                break
            full(board)
            turn = 'o' if turn == 'x' else 'x'
        except EndGame:
            print('nessuno ha vinto :(')


if __name__ == '__main__':
    main(sys.argv[1:])
