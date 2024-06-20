import random

def number_guesser():
    min_num = int(input("Enter minimum number of the range: "))
    max_num = int(input("Enter maximum number of the range: "))
    
    # Get a random number between the specified range (inclusive of min_num, exclusive of max_num)
    randomNumber = random.randrange(min_num, max_num)

    print("Guess the number between specified range")

    # Loop until the user guesses the correct number
    while True:
        # Prompt user to enter their guess
        guess = int(input("Enter number: "))

        # Check if the guess is higher than the random number
        if guess > randomNumber:
            print("Too high! Please try again.")
        # Check if the guess is lower than the random number
        elif guess < randomNumber:
            print("Too low! Please try again.")
        # If the guess is correct
        else:
            print("Hooray! You guessed the number")
            break


# Call the function to execute the number guessing game
number_guesser()
