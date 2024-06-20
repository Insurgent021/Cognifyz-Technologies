import random

def guess_the_num():
    # Get a random number between 1 and 100 (inclusive)
    random_number = random.randint(1, 100)

    print("Guess the number between 1 to 100")
    
    while True:
        # Prompt user to enter their guess
        guess = int(input("Enter number: "))

        # Check if the guess is correct
        if guess == random_number:
            print("Hooray! You guessed the number.")
            break
        # Check if the guess is within 10 numbers higher than the random number
        elif guess in range(random_number + 1, random_number + 10 + 1):
            print("Too high! Please try again.")
        # Check if the guess is within 10 numbers lower than the random number
        elif guess in range(random_number - 10, random_number):
            print("Too low! Please try again.")
        # If the guess is neither close nor correct
        else:
            print("Incorrect! Please try again")


# Execute the function to start the game
guess_the_num()
