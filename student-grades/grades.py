

def add_student(my_dict):
    while True:
        name = input("Enter the student's name: ").title()
        if name == "":
            print("Enter a valid name.")
            continue
        grade = input("Enter the student's grade: ")
        try:
            grade = float(grade)
        except ValueError:
            print("Grade should be a number.")
            continue
        my_dict.update({name: grade})
        again = input("Add/Update another student? (y/n) ").lower()
        if again == "y":
            continue
        elif again == "n":
            break
        else:
            print("Invalid input.")
            break


def check_student(my_dict):
    while True:
        name = input("Enter the student's name to check: ").title()
        if name in my_dict.keys():
            print(f"{name}'s grade is = {my_dict.get(name)}")
        else:
            print("That student doesn't exist!")
        again = input("Check another student? (y/n) ").lower()
        if again == "y":
            continue
        elif again == "n":
            break
        else:
            print("Invalid input.")
            break


def main():
    grades = {}
    while True:
        print("**** WELCOME ****")
        print("\n 1. Add a Student")
        print("\n 2. Check a Student")
        print("\n 3. Exit")

        choice = input("\n Choose an option (1-3): ")
        if choice == "1":
            add_student(grades)
        elif choice == "2":
            check_student(grades)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()
