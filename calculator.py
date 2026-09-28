# Calculator Master - JC Nazareno
# ITNT415 - BIT42

def add(a, b):
    """Return the sum of a and b."""
    pass


def subtract(a, b):
    """Return a minus b."""
    pass


def multiply(a, b):
    """Return the product of a and b."""
    pass


def divide(a, b):
    """Return a divided by b."""
    pass


def show_menu():
    print("\n=== Calculator Master ===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            break
        elif choice in ("1", "2", "3", "4"):
            print("This operation is not implemented yet.")
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
