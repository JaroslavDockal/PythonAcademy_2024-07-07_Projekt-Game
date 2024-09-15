"""
druhý projekt do Engeto Online Python Akademie

author: Jaroslav Dočkal

email: jaroslav.dockal@outlook.com

discord: jaroslav.dockal
"""


def displayMenu():
    print("Welcome to the Game Selector!")
    print("1. Play Bulls and Cows")
    print("2. Play Tic-Tac-Toe")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    return choice


def playBullsAndCows():
    import BullsNCows
    BullsNCows.bullsAndCowsGame()


def playTicTacToe():
    import TicTacToe
    TicTacToe.ticTacToeGame()


def main():
    while True:
        choice = displayMenu()

        if choice == '1':
            playBullsAndCows()
        elif choice == '2':
            playTicTacToe()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 3.")


if __name__ == "__main__":
    main()
