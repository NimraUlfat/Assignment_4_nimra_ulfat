# Tic-Tac-Toe Game in Python

# Function to display the board
def display_board(board):
    print(f"\n{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}\n")

# Function to check if a player has won
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Middle column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Diagonal (top-left to bottom-right)
        [2, 4, 6],  # Diagonal (top-right to bottom-left)
    ]
    
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all(space != " " for space in board)

# Main function to play the game
def play_game():
    board = [" " for _ in range(9)]  # Initialize empty board
    current_player = "X"  # Player X always starts

    while True:
        display_board(board)
        
        # Get the move from the current player
        move = input(f"Player {current_player}, choose a position (1-9): ")
        
        # Check if the input is valid (between 1 and 9, and not already taken)
        try:
            move = int(move) - 1  # Convert to 0-indexed
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move! Try again.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")
            continue
        
        # Make the move
        board[move] = current_player
        
        # Check for a winner
        if check_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins! 🎉")
            break
        
        # Check for a tie
        if is_board_full(board):
            display_board(board)
            print("It's a tie! 🤝")
            break
        
        # Switch to the other player
        current_player = "O" if current_player == "X" else "X"

# Run the game
if __name__ == "__main__":
    play_game()
