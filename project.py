def main():
    # Create a 3x3 array that represents our tic tac toe board
    board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    # ask the players for their names
    print("Let's play Tic Tac Toe!")
    p1 = input("Player 1, what is your name? ")
    p2 = input("Player 2, what is your name? ")

    # Create a player1 boolean that is true if it is player 1's turn and false if it is player 2's turn
    player1 = True

    # Create a gameEnded boolean and use it as the condition in the while loop
    gameEnded = False

    while not gameEnded:

        # draw the board
        draw_board(board)

        # print whose turn it is
        if player1:
            print(f"{p1}'s turn (x): ")
        else:
            print(f"{p2}'s turn (o): ")

        # create a char variable that stores either 'x' or 'o' based on what player's turn it is
        c = '-'
        if player1:
            c = 'x'
        else:
            c = 'o'

        # create row and col variables which represent indexes that correspond to a position on our board
        row = col = 0

        # Only break out of the while loop once the user enters a valid position
        while True:
            # ask the user for what position they want to place their x or o
            row = int(input('Enter a row number (0, 1, or 2): '))
            col = int(input('Enter a column number (0, 1, or 2): '))

            # Check if the row and col are 0, 1, or 2
            if row < 0 or col < 0 or row > 2 or col > 2:
                print('This position is off the bounds of the board! Try again.')
            # Check if the position on the board the user entered is empty (has a -) or not
            elif board[row][col] != '-':
                print('Someone has already made a move at this position! Try again.')
            # Otherwise, the position is valid so break out of the while loop
            else:
                break

        # Set the position on the board at row, col to c
        board[row][col] = c

        # Check to see if either player has won

        if player_has_won(board) == 'x':
            print(f"{p1} has won!")
            gameEnded = True
        elif player_has_won(board) == 'o':
            print(f"{p2} has won!")
            gameEnded = True
        else:
            # if neither player has won, check to see if there has been a tie (if the board is full)
            if board_is_full(board):
                print("It's a tie!")
                gameEnded = True
            else:
                # If player1 is true, make it false, and vice versa; this way, the players alternate each turn
                player1 = not player1

    # Draw the board at the end of the game
    draw_board(board)

# draw the tic tac toe board
def draw_board(board):
    print('Board:')
    for i in range(3):
        for j in range(3):
            print(board[i][j], end='')
        print()

# see if someone has won and return the winning char
def player_has_won(board):

    # check each row
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != '-':
            return board[i][0]

    # check each column
    for j in range(3):
        if board[0][j] == board[1][j] and board[1][j] == board[2][j] and board[0][j] != '-':
            return board[0][j]

    # Check the diagonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != '-':
        return board[0][0]

    if board[2][0] == board[1][1] and board[1][1] ==  board[0][2] and board[2][0] != '-':
        return board[2][0]

    # Otherwise nobody has not won yet
    return ' '

# check if all of the positions on the board have been filled
def board_is_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                return False

    return True

if __name__ == '__main__':
    main()