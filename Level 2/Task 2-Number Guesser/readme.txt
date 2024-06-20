# Number Guesser Game

This is a simple number guessing game implemented in Python. The user needs to guess a randomly generated number within a specified range.

## How to Play

1. Run the program.
2. Enter the minimum and maximum number for the guessing range.
3. Try to guess the randomly generated number.
4. The program will provide feedback if the guess is too high or too low.
5. Continue guessing until the correct number is guessed.

## Code Explanation

- The program uses the `random` module to generate a random number within a specified range.
- It prompts the user to enter the minimum and maximum values for the range.
- It then enters a loop, repeatedly asking the user to guess the number, providing feedback until the correct number is guessed.

## Example

Enter minimum number of the range: 1
Enter maximum number of the range: 100
Guess the number between specified range
Enter number: 50
Too high! Please try again.
Enter number: 25
Too low! Please try again.
Enter number: 37
Hooray! You guessed the number