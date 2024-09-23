"""
Druhý projekt do Engeto Online Python Akademie

author: Jaroslav Dočkal

email: jaroslav.dockal@outlook.com

discord: jaroslav.dockal
"""


def displayMenu():
    """
    Displays the game selection menu and prompts the user to make a choice.

    Returns:
        str: The user's choice as a string ('1' for Bulls and Cows, '2' for Tic-Tac-Toe, '3' to exit).
    """
    print("Welcome to the Game Selector!")
    print("1. Play Bulls and Cows")
    print("2. Play Tic-Tac-Toe")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    return choice


def playBullsAndCows():
    """
    Imports and starts the Bulls and Cows game by calling the main game function.
    """
    import BullsNCows
    BullsNCows.bullsAndCowsGame()


def playTicTacToe():
    """
    Imports and starts the Tic-Tac-Toe game by calling the main game function.
    """
    import TicTacToe
    TicTacToe.ticTacToeGame()


def main():
    """
    Main function to handle the game selection logic.
    Continuously displays the menu until the user chooses to exit.
    """
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
