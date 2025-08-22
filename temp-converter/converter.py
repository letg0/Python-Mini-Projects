while True:
    temp = input("Enter the temperature (q to quit): ")
    if temp.lower() == "q":
        print("Goodbye!")
        break
    try:
        temp = float(temp)
    except ValueError:
        print(f"{temp} is not a valid number")
        continue
    while True:
        unit = input("Enter a unit for the temperature (C/F): ").upper()
        if unit == "C":
            print(f"{temp}° Celsius is equal to {(temp * 9 / 5) + 32}° Fahrenheit")
            break
        elif unit == "F":
            print(f"{temp}° Fahrenheit is equal to {(temp - 32) * 5 / 9}° Celsius")
            break
        else:
            print("That is not a valid unit.")
