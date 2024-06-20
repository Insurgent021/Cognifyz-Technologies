def fibonacci_series(num):
    # Initialize the first two Fibonacci numbers
    fi = 0
    fj = 1
    # Initialize the counter
    i = 1

    print("The Fibonacci sequence is: ")
    
    # Print the first term if num is greater than 0
    if num > 0:
        print(fi, end=" ")

    # Print the second term if num is greater than 1
    if num > 1:
        print(fj, end=" ")

    # Loop to calculate and print the next Fibonacci numbers
    while i < num - 1:
        # Calculate the next Fibonacci number
        fk = fi + fj
        # Print the next Fibonacci number
        print(fk, end=" ")
        # Update the previous two Fibonacci numbers
        fi = fj
        fj = fk
        # Increment the counter
        i += 1


num = int(input("Enter the number of terms of Fibonacci sequence: "))

# Call the function to generate the Fibonacci sequence
fibonacci_series(num)
