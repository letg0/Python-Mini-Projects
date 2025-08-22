class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        print(f"\n Your Balance = ${self.balance:.2f}")

    def get_amount(self, prompt):
        while True:
            value = input(prompt)
            if value.lower() == 'q':
                return None
            try:
                value = float(value)
                if value <= 0:
                    print("Enter a positive number!")
                    continue
                return value
            except ValueError:
                print(f"{value} is not a number!")

    def deposit(self):
        amount = self.get_amount(
            "Enter an amount to deposit (or 'q' to cancel): $")
        if amount is None:
            return
        self.balance += amount
        print(f"Deposit successful! New balance: ${self.balance:.2f}")

    def withdraw(self):
        amount = self.get_amount(
            "Enter an amount to withdraw (or 'q' to cancel): $")
        if amount is None:
            return
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdraw successful! New balance: ${self.balance:.2f}")


def main():
    is_running = True
    account = BankAccount(0)
    while is_running:
        print("\n *******************************")
        print("\n WELCOME TO PYTHON BANKING PROGRAM!")
        print("\n *******************************")

        print("\n 1. Check Balance")
        print("\n 2. Deposit Money")
        print("\n 3. Withdraw Money")
        print("\n 4. Exit")
        ui = input("\n \n Select an option (1-4): ")
        if ui == "1":
            account.check_balance()
        elif ui == "2":
            account.deposit()
        elif ui == "3":
            account.withdraw()
        elif ui == "4":
            print("\n BYE!")
            is_running = False
        else:
            print("\n Invalid input.")
            continue


if __name__ == "__main__":
    main()
