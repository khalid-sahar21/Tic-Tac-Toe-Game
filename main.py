import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != ' ':
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

    return False

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def get_player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if 1 <= move <= 9:
                return move
            else:
                print("Invalid move. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = random.choice(players)

    print("Welcome to Tic Tac Toe!")

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        if current_player == 'O':
            move = get_player_move()
        else:
            move = random.randint(1, 9)

        row, col = divmod(move - 1, 3)

        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print("Invalid move. The cell is already occupied. Try again.")
            continue

        if check_winner(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_tic_tac_toe()
