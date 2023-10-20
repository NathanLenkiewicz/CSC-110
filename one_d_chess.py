def create_board():
    board = ["WKi", "WKn", "WKn", 
                    "EMPTY", "EMPTY", "EMPTY",
                    "BKn", "BKn", "BKi"]
    return board

board = create_board()

def printable_board(board):
    top = "+-----------------------------------------------------+\n"
    bottom = "+-----------------------------------------------------+"
    string_board = ""
    for i in range(len(board)):
        if board[i] != "EMPTY":
            string_board += "| " + board[i] + " "
        else:
            string_board += " | " + " "*3
    string_board += "|"
    return (top + string_board + "\n" + bottom)

def is_valid_move(board, position, player):
    if position in range(len(board)):
        if board[position] != "EMPTY" and board[position][0] == player[0]:
            return True
    return False

def move_king(board, position, direction):
    pass