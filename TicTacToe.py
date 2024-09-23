def printIntro():
    """
    Prints the introduction to the Tic-Tac-Toe game.
    """
    print("============================================")
    print("Welcome to Tic-Tac-Toe!")
    print("============================================")
    print("GAME RULES:")
    print("Each player can place one mark (or stone)")
    print("per turn on the 3x3 grid. The WINNER is")
    print("who succeeds in placing three of their")
    print("marks in a horizontal, vertical or diagonal row.")
    print("============================================")
    print("Let's start the game!")

def initializeBoard():
    """
    Initializes and returns a 3x3 Tic-Tac-Toe board as a list of lists.
    Each cell in the board is initialized to a space character (' ').

    Returns:
        list: A 3x3 list representing the Tic-Tac-Toe board.
    """
    return [[' ' for _ in range(3)] for _ in range(3)]


def drawBoard(board):
    """
    Draws the current state of the Tic-Tac-Toe board.

    Args:
        board (list): A 3x3 list representing the Tic-Tac-Toe board.
    """
    for i in range(3):
        print("+---+---+---+")
        print(f"| {board[i][0]} | {board[i][1]} | {board[i][2]} |")
    print("+---+---+---+")


def validateMove(board, move):
    """
    Validates whether the player's move is allowed (i.e., the spot is not already taken).
    Checks for valid input and ensures that the cell is within bounds and empty.

    Args:
        board (list): A 3x3 list representing the Tic-Tac-Toe board.
        move (tuple): A tuple (row, col) representing the player's desired move.

    Returns:
        bool: True if the move is valid, False otherwise.
    """
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
    """
    Checks if there is a winner on the Tic-Tac-Toe board.
    A player wins by having three of their marks ('X' or 'O') in a row, column, or diagonal.

    Args:
        board (list): A 3x3 list representing the Tic-Tac-Toe board.

    Returns:
        str: 'X' if player X wins, 'O' if player O wins, or None if there is no winner.
    """
    lines = (
        board[0], board[1], board[2],  # Rows
        [board[i][0] for i in range(3)], [board[i][1] for i in range(3)], [board[i][2] for i in range(3)],  # Columns
        [board[i][i] for i in range(3)], [board[i][2 - i] for i in range(3)]  # Diagonals
    )

    for line in lines:
        if all(cell == 'X' for cell in line):
            return 'X'
        elif all(cell == 'O' for cell in line):
            return 'O'

    return None


def ticTacToeGame():
    """
    Runs the Tic-Tac-Toe game. Players X and O take turns entering their move, and the board
    is updated after each valid move. The game continues until there is a winner or a tie.
    """
    printIntro()
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
            print("============================================")
            print(f"Congratulations, Player {winner} wins!")
            print("============================================")
            break
        elif all(all(cell != ' ' for cell in row) for row in board):
            drawBoard(board)
            print("It's a tie!")
            break

        currentPlayer = 'O' if currentPlayer == 'X' else 'X'


if __name__ == "__main__":
    ticTacToeGame()
