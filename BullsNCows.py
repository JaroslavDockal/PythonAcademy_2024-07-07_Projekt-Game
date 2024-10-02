import random
import time


def generateSecretNumber():
    """
    Generates a random 4-digit number with unique digits.
    Ensures that the first digit is not 0.

    Returns:
        str: A string representing the secret 4-digit number.
    """
    digits = random.sample(range(10), 4)
    if digits[0] == 0:
        digits[0], digits[1] = digits[1], digits[0]
    return ''.join(map(str, digits))


def validateGuess(guess):
    """
    Validates the player's guess. The guess must be a 4-digit number,
    must not start with 0, and must not contain duplicate digits.

    Args:
        guess (str): The player's guessed number.

    Returns:
        bool: True if the guess is a valid 4-digit number, False otherwise.
    """
    if not guess.isdigit():
        print("Invalid input. Please enter only numbers.")
        return False
    if len(guess) != 4:
        print("Invalid input. Please enter exactly 4 digits.")
        return False
    if guess[0] == '0':
        print("Invalid input. The number cannot start with 0.")
        return False
    if len(set(guess)) != 4:
        print("Invalid input. The digits must not repeat.")
        return False
    return True


def evaluateGuess(guess, secretNumber):
    """
    Compares the player's guess to the secret number and calculates bulls and cows.

    Bulls are digits in the correct position, cows are digits that exist in the number
    but are in the wrong position.

    Args:
        guess (str): The player's guessed number.
        secretNumber (str): The secret number to be guessed.

    Returns:
        tuple: A tuple containing the number of bulls and cows.
    """
    bulls, cows = 0, 0
    for i in range(4):
        if guess[i] == secretNumber[i]:
            bulls += 1
        elif guess[i] in secretNumber:
            cows += 1
    return bulls, cows


def bullsAndCowsGame():
    """
    Runs the Bulls and Cows game. Generates a secret number, takes input from the player,
    and evaluates their guess. The game continues until the player guesses the secret number.

    Tracks the number of attempts and the time taken to guess the correct number.
    """
    print("Welcome to the Bulls and Cows game!")
    secretNumber = generateSecretNumber()
    attempts = 0
    startTime = time.time()

    while True:
        guess = input("Enter your 4-digit guess: ")
        attempts += 1

        if not validateGuess(guess):
            continue

        bulls, cows = evaluateGuess(guess, secretNumber)

        if bulls == 4:
            endTime = time.time()
            timeTaken = round(endTime - startTime, 2)
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            print(f"Time taken: {timeTaken} seconds.")
            break

        bull_str = "bull" if bulls == 1 else "bulls"
        cow_str = "cow" if cows == 1 else "cows"
        print(f"{bulls} {bull_str}, {cows} {cow_str}")


if __name__ == "__main__":
    bullsAndCowsGame()
