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
    # 8 is the highest possible index (furtherst
    # right)
    # 0 is the furthest left position
    # position is the piece being moved
    if direction == "LEFT": 
        for i in range(len(board)):
            if (board[position-i] != "EMPTY"):
                board[position-1] = board[position]
        board[position] = "EMPTY"
    return board

move_king(board, 0, "RIGHT")
print( printable_board(board) )

#print(move_king(board, 2, "RIGHT"))