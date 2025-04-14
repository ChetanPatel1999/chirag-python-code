# Show operation menu
print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Take operation choice
choice = int(input("Enter choice (1/2/3/4): "))

# match-case structure with input inside cases
match choice:
    case 1:
        num1 = eval(input("Enter first number: "))
        num2 = eval(input("Enter second number: "))
        sum=num1+num2
        print(f"Result: {num1} + {num2} = {sum}")

    case 2:
        num1 = eval(input("Enter first number: "))
        num2 = eval(input("Enter second number: "))
        sub=num1 - num2
        print(f"Result: {num1} - {num2} = {sub}")

    case 3:
        num1 = eval(input("Enter first number: "))
        num2 = eval(input("Enter second number: "))
        print(f"Result: {num1} * {num2} = {num1 * num2}")

    case 4:
        num1 = eval(input("Enter first number: "))
        num2 = eval(input("Enter second number: "))
        if num2 != 0:
            print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Cannot divide by zero.")

    case _:
        print("Invalid input! Please choose between 1 and 4.")
