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
