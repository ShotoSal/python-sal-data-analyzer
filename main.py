def main():
    print("Python CLI Data Analyzer")
    
    # Ask the user how many numbers to enter
    try:
        count = int(input("How many numbers would you like to enter? "))
        if count <= 0:
            print("Please enter a positive number.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    numbers = []

    # Loop to collect inputs
    for i in range(count):
        while True:
            try:
                num = float(input(f"Enter number {i + 1}: "))
                numbers.append(num)  # Store numbers in a list
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # Print the list
    print("You entered the following numbers:", numbers)

if __name__ == "__main__":
    main()