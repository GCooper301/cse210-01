# Garrett Cooper 
# Tic-Tac-Toe

#main function
def main():
    player = next_player("")
    board = make_board()
    while not (winner(board) or tie(board)):
        draw_board(board)
        player_turn(player, board) 
        player = next_player(player)
    if (winner(board)) == True:
        draw_board(board)
        print("Good game, thank you for playing!")
    elif (tie(board)) == True:
        draw_board(board)
        print("It's a tie, thank you for playing!")

#create board to be played on
def make_board(): 
    board = []
    for i in range(9):
        board.append(i + 1)
    return board

#display board and printed below
def draw_board(board):
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-----")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-----")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print("-----")

#create funtion that decides a winner
def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

#funtion for a tie game
def tie(board):
    for i in range(9):
        if board[i] !="X" and board[i] != "O":
            return False
    return True

#funtion to define players turn
def player_turn(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player

#funtion to difine player to choose a square
def next_player(current):
    if current == "" or current == "O":
        return "X"
    elif current == "X":
        return "O"

if __name__ == "__main__":
    main()