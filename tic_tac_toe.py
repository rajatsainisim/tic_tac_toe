import random

# Display the board
def display_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]}")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]}")

# Check for win
def check_winner(board, symbol):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == symbol:
            return True
    return False

# Check for draw
def check_draw(board):
    return ' ' not in board

# Get valid moves
def get_valid_moves(board):
    return [i for i in range(9) if board[i] == ' ']

# Get player input
def player_move(board, player_name, symbol):
    while True:
        try:
            move = int(input(f"{player_name}, enter your move (1-9): ")) - 1
            if move in get_valid_moves(board):
                board[move] = symbol
                break
            else:
                print("Invalid move, position already taken or out of range. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

# Basic AI for the computer to choose random moves
def computer_move(board, symbol):
    valid_moves = get_valid_moves(board)
    move = random.choice(valid_moves)
    board[move] = symbol
    print(f"Computer plays at position {move + 1}")

# Setup players
def setup_players():
    player1_name = input("Enter Player 1's name: ")
    player1_symbol = input(f"{player1_name}, choose your symbol (O or X, default is O): ").upper()
    if player1_symbol not in ['X', 'O']:
        player1_symbol = 'O'

    opponent_type = input("Will Player 2 be (H)uman or (C)omputer? ").upper()
    
    if opponent_type == 'H':
        player2_name = input("Enter Player 2's name: ")
        player2_symbol = 'X' if player1_symbol == 'O' else 'O'
    else:
        player2_name = "Computer"
        player2_symbol = 'X' if player1_symbol == 'O' else 'O'

    return player1_name, player1_symbol, player2_name, player2_symbol

# Main game loop
def play_game():
    board = [' '] * 9
    player1_name, player1_symbol, player2_name, player2_symbol = setup_players()

    display_board(board)
    
    current_player, current_symbol = player1_name, player1_symbol
    
    while True:
        if current_player == "Computer":
            computer_move(board, current_symbol)
        else:
            player_move(board, current_player, current_symbol)
        
        display_board(board)

        # Check for win or draw
        if check_winner(board, current_symbol):
            print(f"Congratulations! {current_player} wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

        # Switch player
        if current_player == player1_name:
            current_player, current_symbol = player2_name, player2_symbol
        else:
            current_player, current_symbol = player1_name, player1_symbol

# Run the game
if __name__ == "__main__":
    play_game()
