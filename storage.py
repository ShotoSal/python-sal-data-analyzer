# storage.py
import json

def save_numbers(numbers, filename="data.json"):
    """
    Save the list of numbers to a JSON file as:
    { "numbers": [...] }
    """
    data = {"numbers": numbers}

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
