import random

def generate_board(size, bombs):
    board = [[0 for _ in range(size)] for _ in range(size)]
    bomb_spots = random.sample(range(size*size), bombs)
    
    for spot in bomb_spots:
        row = spot // size
        col = spot % size
        board[row][col] = 'X'
        
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                if 0 <= i < size and 0 <= j < size and board[i][j] != 'X':
                    board[i][j] += 1
                    
    return board

def print_board(board, revealed):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if revealed[i][j]:
                if board[i][j] == 'X':
                    print("X", end=" ")
                else:
                    print("0", end=" ")
            else:
                print("?", end=" ")
        print("\n")

def open_cell(board, revealed, row, col):
    if revealed[row][col]:
        return
    revealed[row][col] = True
    
    if board[row][col] == 0:
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                if 0 <= i < len(board) and 0 <= j < len(board[0]):
                    open_cell(board, revealed, i, j)

def check_win(board, revealed):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 'X' and not revealed[i][j]:
                return False
    return True

def play_game():
    size = 3
    bombs = 1
    board = generate_board(size, bombs)
    revealed = [[False for _ in range(size)] for _ in range(size)]
    print(f"========================================================\n")
    print_board(board, revealed)
    while True:
        print(f"========================================================\n")
        row = int(input("Enter row(1-3): ")) - 1
        col = int(input("Enter column(1-3): ")) - 1
        
        if board[row][col] == 'X':
            print("Yikes, you found a bomb. The end :(")
            print(f"\n========================================================\n")
            open_cell(board, revealed, row, col)
            print_board(board, revealed)
            print(f"========================================================\n")
            break
        else:
            print("Well, there's no bomb here. Congrats!")
            print(f"\n========================================================\n")
            open_cell(board, revealed, row, col)
            print_board(board, revealed)
            
            if check_win(board, revealed):
                print("Congratulations! You won!")
                print(f"========================================================")
                break

play_game()
