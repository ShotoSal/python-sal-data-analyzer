from storage import save_numbers
from datetime import datetime

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

    # Save dataset to JSON
    save_numbers(numbers)
    print("Numbers saved to data.json")


    # ===== Commit 4: Save report to file =====
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("report.txt", "w") as file:
        file.write(f"Analysis Report - {timestamp}\n")
        file.write(str(report))

    print("Report saved to report.txt")


# REQUIRED bottom guard
if __name__ == "__main__":
    main()
