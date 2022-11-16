def display_board(board):
    print("\t{0} | {1} | {2}".format(board[0], board[1], board[2]))
    print("\t_ | _ | _")
    print("\t{0} | {1} | {2}".format(board[3], board[4], board[5]))
    print("\t_ | _ | _")
    print("\t{0} | {1} | {2}".format(board[6], board[7], board[8]))


def legal_moves(board):
    """Returns the list of available positions"""
    moves = []
    for i in range(9):
        if board[i] in list("012345678"):
            moves.append(i)
    return moves


def getPlayerMove(board):
    move = 9
    while move not in legal_moves(board):
        move = int(input("Please select the drop position (0-8):"))
    return move


def getComputerMove(board, computerLetter, playerLetter):
    boardcopy = board.copy()

    for move in legal_moves(boardcopy):
        boardcopy[move] = computerLetter
        if isWinner(boardcopy):
            return move
        boardcopy[move] = str(move)
    
    for move in legal_moves(boardcopy):
        boardcopy[move] = playerLetter
        if isWinner(boardcopy):
            return move
        boardcopy[move] = str(move)
    
    for move in (4,0,2,6,8,1,3,5,7):
        if move in legal_moves(board):
            return move
        
def isWinner(board):
    WIN = {(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)}
    for r in WIN:
        if board[r[0]] == board[r[1]] == board[r[2]]:
            return True
    return False


def isDraw(board):
    for i in list("012345678"):
        if i in board:
            return False
    return True

board = list("012345678")

def tic_tac_toe():
    playerLetter = input("please choose'X'and'O',X goes first" )
    if playerLetter in ("X"):
        turn = "player"
        playerLetter = "X"
        computerLetter ="O"
    else:
        turn = "computer"
        computerLetter = "X"
        playerLetter = "O"
    print("{}goes first".format(turn))
    
    while True:
            display_board(board)
            if turn == 'player':
                move = getPlayerMove(board)
                board[move] = playerLetter
                if isWinner(board):
                    display_board(board)
                    print("Player Won")
                    break
                else:
                    turn = "computer"
            else:
                move = getComputerMove(board, computerLetter, playerLetter)
                print("Computer choose", move)
                board[move] = computerLetter
                if isWinner(board):
                    display_board(board)
                    print("Computer Win")
                    break
                else:
                    turn = "player"

            if isDraw(board):
                display_board(board)
                print('Draw')
                break

if __name__ == '__main__':
    tic_tac_toe()

