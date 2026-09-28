# Calculator Master - John Cyrel Nazareno
# ITNT415 - BIT42


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return a minus b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a divided by b. Raises ZeroDivisionError if b is 0."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def show_menu():
    print("\n=== Calculator Master ===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")


def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            break
        elif choice == "1":
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            print(f"Result: {a} + {b} = {add(a, b)}")
        elif choice == "2":
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            print(f"Result: {a} - {b} = {subtract(a, b)}")
        elif choice == "3":
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            print(f"Result: {a} x {b} = {multiply(a, b)}")
        elif choice == "4":
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            try:
                print(f"Result: {a} / {b} = {divide(a, b)}")
            except ZeroDivisionError:
                print("Error: Cannot divide by zero.")
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()