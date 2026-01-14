import math

def median(values):
    """Return the median of a list of numbers."""
    if not values:
        return None

    sorted_vals = sorted(values)
    n = len(sorted_vals)
    mid = n // 2

    if n % 2 == 1:
        return sorted_vals[mid]
    return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2


def std_dev(values):
    """Return the population standard deviation of a list of numbers."""
    if not values:
        return None

    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    return math.sqrt(variance)


def analyze_time_series(times, temperatures):
    """
    Analyze hourly temperature series and return descriptive statistics.
    times: list[str]
    temperatures: list[float]
    """
    if not temperatures:
        return {
            "count": 0,
            "min": None,
            "max": None,
            "mean": None,
            "median": None,
            "std_dev": None
        }

    return {
        "count": len(temperatures),
        "min": min(temperatures),
        "max": max(temperatures),
        "mean": sum(temperatures) / len(temperatures),
        "median": median(temperatures),
        "std_dev": std_dev(temperatures)
    }
