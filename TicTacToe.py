def initializeBoard():
    return [[' ' for _ in range(3)] for _ in range(3)]

def drawBoard(board):
    for i in range(3):
        print("+---+---+---+")
        print(f"| {board[i][0]} | {board[i][1]} | {board[i][2]} |")
    print("+---+---+---+")

def validateMove(board, move):
    try:
        row, col = move
        if board[row][col] == ' ':
            return True
        else:
            print("That spot is taken. Choose an empty spot.")
            return False
    except IndexError:
        print("Invalid input. Choose a number between 1 and 9.")
        return False
    except ValueError:
        print("Invalid input. Choose a number between 1 and 9.")
        return False

def checkWinner(board):
    lines = (
        board[0], board[1], board[2],  # rows
        [board[i][0] for i in range(3)], [board[i][1] for i in range(3)], [board[i][2] for i in range(3)],  # columns
        [board[i][i] for i in range(3)], [board[i][2-i] for i in range(3)]  # diagonals
    )

    for line in lines:
        if all(cell == 'X' for cell in line):
            return 'X'
        elif all(cell == 'O' for cell in line):
            return 'O'

    return None

def ticTacToeGame():
    print("============================================")
    print("Welcome to Tic-Tac-Toe!")
    print("============================================")

    board = initializeBoard()
    currentPlayer = 'X'
    moveMapping = {
        '1': (0, 0), '2': (0, 1), '3': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '7': (2, 0), '8': (2, 1), '9': (2, 2)
    }

    while True:
        drawBoard(board)
        print(f"Player {currentPlayer}, enter your move (1-9): ", end='')
        move = input()

        if move not in moveMapping:
            print("Invalid input. Choose a number between 1 and 9.")
            continue

        row, col = moveMapping[move]
        if not validateMove(board, (row, col)):
            continue

        board[row][col] = currentPlayer
        winner = checkWinner(board)

        if winner:
            drawBoard(board)
            print(f"Player {winner} wins!")
            break
        elif all(all(cell != ' ' for cell in row) for row in board):
            drawBoard(board)
            print("It's a tie!")
            break

        currentPlayer = 'O' if currentPlayer == 'X' else 'X'


if __name__ == "__main__":
    ticTacToeGame()
