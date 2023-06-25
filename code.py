# Tic Tac Toe

# Function to print the board
def print_board(board):
    print("-------------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, end=" | ")
        print("\n-------------")

# Function to check if any player has won
def check_winner(board):
    # Check rows
    for row in board:
        if len(set(row)) == 1 and row[0] != ' ':
            return row[0]

    # Check columns
    for col in range(3):
        if len(set([board[row][col] for row in range(3)])) == 1 and board[0][col] != ' ':
            return board[0][col]

    # Check diagonals
    if (board[0][0] == board[1][1] == board[2][2] != ' ') or (board[0][2] == board[1][1] == board[2][0] != ' '):
        return board[1][1]

    return None

# Function to play the game
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    winner = None

    while not winner:
        print_board(board)

        # Get player's move
        while True:
            move = input(f"Player {current_player}, enter your move (row[1-3] column[1-3]): ")
            row, col = map(int, move.split())

            # Check if the move is valid
            if row in range(1, 4) and col in range(1, 4) and board[row - 1][col - 1] == ' ':
                break
            else:
                print("Invalid move. Please try again.")

        # Update the board with the player's move
        board[row - 1][col - 1] = current_player

        # Check if the current player has won
        winner = check_winner(board)

        # Switch to the next player
        current_player = 'O' if current_player == 'X' else 'X'

    # Print the final board and the winner
    print_board(board)
    print(f"Player {winner} wins!")

# Start the game
play_game()


#instructions
# To play the game, simply run the script. Players will take turns entering their moves by specifying the row and column numbers 
# (both ranging from 1 to 3). The game will continue until one of the players wins or the game ends in a draw.
