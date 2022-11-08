from logic import *
if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    player = 'O'
    while winner == None:
        print("TODO: take a turn!")
        # TODO: Show the board to the user.
        print(print_board(board))
        # TODO: Input a move from the player.
        command = input("Player %s, please take a move: " % player)
        # TODO: Update the board.
        error = make_move(board, player, command)
        # TODO: Update who's turn it is. Decide who is the winner.
        if not error:
            player = other_player(player)
        else:
            if error == 1:
                print("Illegal position! Please input the number less than 9!")
            elif error == 2:
                print("The cell has already been taken! Try another.")
            continue
        winner = get_winner(board)
        if winner is not None:
            if winner == 'Draw':
                print(print_board(board))
                print('Draw!')
            else:
                print("%s won!" % winner)