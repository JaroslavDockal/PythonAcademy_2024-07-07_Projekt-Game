import random
import time


def generateSecretNumber():
    return str(random.randint(1023, 9876))


def validateGuess(guess, secretNumber):
    return guess.isdigit() and len(guess) == 4


def evaluateGuess(guess, secretNumber):
    bulls, cows = 0, 0
    for i in range(4):
        if guess[i] == secretNumber[i]:
            bulls += 1
        elif guess[i] in secretNumber:
            cows += 1
    return bulls, cows

def bullsAndCowsGame():
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
