class EndGame(Exception): pass


def row(board, i):
    return ''.join(board[i])


def col(board, i):
    return ''.join((board[0][i], board[1][i], board[2][i]))


def oblique(board, i):
    if i == 0:
        elements = (board[0][0], board[1][1], board[2][2])
    else:
        elements = (board[0][2], board[1][1], board[2][0])
    return ''.join(elements)


def won(elements):
    if elements == 'xxx':
        return True, 'x'
    if elements == 'ooo':
        return True, 'o'
    return False


def win(board):
    for i in range(2):
        winner = won(oblique(board, i))
        if winner:
            return winner
    for i in range(3):
        winner = won(row(board, i))
        if winner:
            return winner
        winner = won(col(board, i))
        if winner:
            return winner
    return False, None


def move(board, x, y, mark):
    if board[x][y]:
        return False
    board[x][y] = mark
    return True


def full(board):
    empty = False
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                return None
    raise EndGame


def init_board():
    board = [
        ['', '', ''],
        ['', '', ''],
        ['', '', ''],
    ]
    return board
