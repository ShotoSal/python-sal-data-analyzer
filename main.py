from storage import save_numbers, load_numbers, save_report
from analyzer import analyze_numbers, print_report


def collect_numbers():
    try:
        count = int(input("How many numbers would you like to enter? "))
        if count <= 0:
            print("Please enter a positive number.")
            return []
    except ValueError:
        print("Invalid input.")
        return []

    numbers = []
    for i in range(count):
        while True:
            try:
                num = float(input(f"Enter number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid number.")

    return numbers


def main():
    numbers = []
    last_results = None

    print("Python CLI Data Analyzer")

    while True:
        print("\nMenu:")
        print("1) Enter numbers")
        print("2) Save numbers to JSON")
        print("3) Load numbers from JSON")
        print("4) Analyze current numbers")
        print("5) Save analysis report to file")
        print("6) Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            numbers = collect_numbers()
            last_results = None

        elif choice == "2":
            save_numbers(numbers)
            print("Numbers saved to data.json")

        elif choice == "3":
            numbers = load_numbers()
            last_results = None
            if numbers:
                print("Numbers loaded:", numbers)
            else:
                print("No saved data found.")

        elif choice == "4":
            last_results = analyze_numbers(numbers)
            print_report(last_results)

        elif choice == "5":
            if last_results is None:
                print("No analysis available. Run option 4 first.")
            else:
                save_report(last_results)
                print("Analysis saved to analysis.txt")

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select 1–6.")


if __name__ == "__main__":
    main()
