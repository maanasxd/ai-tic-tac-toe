import math

# Initialize empty board
board = [' ' for _ in range(9)]

def print_board(b):
    for i in range(0, 9, 3):
        print(f"{b[i]}|{b[i+1]}|{b[i+2]}")

def check_win(b, player):
    win_states = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(b[x] == b[y] == b[z] == player for x, y, z in win_states)

def minimax(b, depth, is_max):
    if check_win(b, 'O'): return 1
    if check_win(b, 'X'): return -1
    if ' ' not in b: return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                best = max(best, minimax(b, depth + 1, False))
                b[i] = ' '
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                best = min(best, minimax(b, depth + 1, True))
                b[i] = ' '
        return best

def computer_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score, move = score, i
    return move

print("TIC-TAC-TOE\nYou are X\nComputer is O")
while True:
    try:
        pos = int(input("Enter position (1-9): ")) - 1
        if pos < 0 or pos > 8 or board[pos] != ' ':
            print("Invalid move. Try again.")
            continue
    except ValueError:
        print("Invalid move. Try again.")
        continue

    board[pos] = 'X'
    if check_win(board, 'X'):
        print_board(board)
        print("You win!")
        break
    if ' ' not in board:
        print_board(board)
        print("Draw!")
        break

    c_move = computer_move()
    board[c_move] = 'O'
    print(f"Computer chose position: {c_move + 1}")
    print_board(board)

    if check_win(board, 'O'):
        print("Computer wins!")
        break
    if ' ' not in board:
        print("Draw!")
        break