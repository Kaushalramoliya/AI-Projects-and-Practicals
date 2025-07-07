'''  
@author: 22000409 Kaushal Ramoliya  
@description: 4. - Write a Program in Python to solve tic-tac-toe problem implementing minimax algorithm. 
'''  
import math

def print_board(board):
    for i in range(3):
        print(" " + " | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("---+---+---")

def is_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]             
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_moves_left(board):
    return ' ' in board

def evaluate(board):
    if is_winner(board, 'O'):
        return 10
    elif is_winner(board, 'X'):
        return -10
    return 0

def minimax(board, depth, is_maximizing):
    score = evaluate(board)
    
    if score == 10 or score == -10:
        return score
    if not is_moves_left(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = max(best, minimax(board, depth + 1, False))
                board[i] = ' '
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = min(best, minimax(board, depth + 1, True))
                board[i] = ' '
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            move_val = minimax(board, 0, False)
            board[i] = ' '
            if move_val > best_val:
                best_val = move_val
                best_move = i
    return best_move

def main():
    board = [' ' for _ in range(9)]
    print("Welcome to Tic Tac Toe!")
    print("You are 'X' and the computer is 'O'.")
    print("Enter your move as row and column numbers .")
    print_board(board)
    
    while True:
        try:
            user_input = input("Enter your move (row col): ")
            row, col = map(int, user_input.split())
            if row < 1 or row > 3 or col < 1 or col > 3:
                print("Invalid input. Row and column numbers must be between 1 and 3.")
                continue
            index = (row - 1) * 3 + (col - 1)
            if board[index] != ' ':
                print("That cell is already occupied. Try another move.")
                continue
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")
            continue

        board[index] = 'X'
        print("\nYour move:")
        print_board(board)

        if is_winner(board, 'X'):
            print("Congratulations! You win!")
            break

        if not is_moves_left(board):
            print("It's a draw!")
            break

        comp_move = find_best_move(board)
        board[comp_move] = 'O'
        print("\nComputer's move:")
        print_board(board)

        if is_winner(board, 'O'):
            print("Computer wins!")
            break

        if not is_moves_left(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()

