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


def validateGuess(guess, secretNumber):
    """
    Validates the player's guess. The guess must be a 4-digit number.

    Args:
        guess (str): The player's guessed number.
        secretNumber (str): The secret number (not used in validation here).

    Returns:
        bool: True if the guess is a valid 4-digit number, False otherwise.
    """
    return guess.isdigit() and len(guess) == 4  # Ensure guess is a 4-digit number


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

        if not validateGuess(guess, secretNumber):
            print("Invalid input. Please enter a 4-digit number.")
            continue

        bulls, cows = evaluateGuess(guess, secretNumber)
        attempts += 1

        if bulls == 4:
            endTime = time.time()
            timeTaken = round(endTime - startTime, 2)
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            print(f"Time taken: {timeTaken} seconds.")
            break

        print(f"Bulls: {bulls}, Cows: {cows}")


if __name__ == "__main__":
    bullsAndCowsGame()
