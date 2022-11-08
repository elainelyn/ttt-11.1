def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],     
    ]

def get_winner(board):
    a = ""
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        a = board[1][1]
    else:
        for i in range(0,3):
            if board[i][0] == board[i][1] == board[i][2]:
                a = board[i][0]
                break
            elif board[0][i] == board[1][i] == board[2][i]:
                    a = board[0][i]
                    break
    if a == "":
        if all([v is not None for rol in board for v in rol]):
            return "Draw"
        else:
            return None
    else:
        return a

def other_player(player):
    return 'O' if player == 'X' else 'X'


def print_board(board):
    s = ''
    for row in board:
        s += '|%s|%s|%s|\n' % (row[0] if row[0] else ' ', row[1] if row[1] else ' ', row[2] if row[2] else ' ')
    return s


def make_move(board, player, command):
    position = int(command)
    if position > 8:
        return 1
    row, col = position // 3, position % 3
    if board[row][col] is not None:
        return 2
    else:
        board[row][col] = player
        return 0
