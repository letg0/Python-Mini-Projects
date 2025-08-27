import random

numbers = []
for num in range(1, 101):
    numbers.append(num)

is_running = True
while is_running:
    answer = random.choice(numbers)
    num_of_guesses = 0
    while True:
        guess = input(
            f"Guess a number between {min(numbers)} and {max(numbers)}: ")
        try:
            guess = int(guess)
        except ValueError:
            print(f"Must enter a number ({min(numbers)}-{max(numbers)})")
            continue
        if guess in numbers:
            if guess > answer:
                print("Too high!")
                num_of_guesses += 1
                continue
            elif guess < answer:
                print("Too low!")
                num_of_guesses += 1
                continue
            else:
                print(f"You guessed it! {answer}")
                num_of_guesses += 1
                if num_of_guesses == 1:
                    print(f"You guessed {num_of_guesses} time")
                else:
                    print(f"You guessed {num_of_guesses} times")
                again = input("Do you want to play again? (y/n): ").lower()
                if again == "y":
                    break
                elif again == "n":
                    is_running = False
                    break
        else:
            print(f"Enter a valid number ({min(numbers)}-{max(numbers)}).")
            continue
