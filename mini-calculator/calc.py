while True:
    num1 = input("Enter the first number: ")
    try:
        num1 = float(num1)
    except ValueError:
        print(f"{num1} is not a number.")
        continue
    while True:
        operator = input("Enter an operator (+-*/): ")
        if operator != "+" and operator != "-" and operator != "*" and operator != "/":
            print("That is not a valid operator")
            continue
        else:
            break
    while True:
        num2 = input("Enter the second number: ")
        try:
            num2 = float(num2)
        except ValueError:
            print(f"{num2} is not a number.")
            continue
        if operator == "+":
            print(num1 + num2)
        elif operator == "-":
            print(num1 - num2)
        elif operator == "*":
            print(num1 * num2)
        elif operator == "/":
            if num2 == 0:
                print("Can't divide by 0!")
                break
            print(num1 / num2)
        break
    again = input("Another calculation? (y/n): ").lower()
    if again == "y":
        continue
