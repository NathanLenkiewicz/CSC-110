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
    if (direction == "RIGHT"):
        for index in range(len(board)-1):
            if index < 8 and direction == "RIGHT":
                if (board[index+1]) == "EMPTY":
                    board[index] = board[position]
                else:
                    board[index+1] = board[position]
                    board[index] = "EMPTY"
                    return board
    if (direction == "LEFT"):
        for j in range(len(board)-1, -1, -1):
            if (j > 0 and direction == "LEFT"):
                if (board[j-1] == "EMPTY"):
                    board[j] = board[position]
                else:
                    board[j-1] = board[position]
                    board[j] = "EMPTY"
                    return board
        

        #print(f"The board at index is {board[i]} and the board at index + 1 is {board[i+1]}")

    #return board
            
print(move_king(board, 0, "LEFT"))
print( printable_board(board) )