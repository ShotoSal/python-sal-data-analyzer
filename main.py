# Define analyze_numbers(numbers)
# Return count, min, max, sum, average in a dictionary
def analyze_numbers(numbers):
    if not numbers:
        return {
            "count": 0,
            "min": None,
            "max": None,
            "sum": 0,
            "average": None
        }

    return {
        "count": len(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers)
    }


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
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # Print the list
    print("You entered the following numbers:", numbers)

    # Call the analysis function
    report = analyze_numbers(numbers)

    # Print the report
    print("Analysis report:")
    print(report)


# REQUIRED bottom guard
if __name__ == "__main__":
    main()
