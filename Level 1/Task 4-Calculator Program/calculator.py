num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
op = input("Enter the operator(+,-,*,/,%): ")

# Using match-case statement to select the operation based on the operator
match op:
    case "+":
        print(f"The addition is {num1 + num2}")
    case "-":
        print(f"The subtraction is {num1 - num2}")
    case "*":
        print(f"The multiplication is {num1 * num2}")
    case "/":
        print(f"The division is {num1 / num2}")
    case "%":
        print(f"The modulus is {num1 % num2}")
    case default:
        print("Invalid operator")
