from flask import Flask, render_template, request, jsonify
from analyzer import analyze_numbers
from external_api import fetch_hourly_temperature
from weather_analysis import analyze_time_series

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    name = "Salman"
    return render_template("index.html", name=name)

@app.route("/analyze", methods=["POST"])
def analyze():
    raw = request.form.get("numbers")

    if not raw:
        return render_template(
            "index.html",
            name="Salman",
            error="Please enter some numbers."
        )

    try:
        # Allow commas or spaces
        parts = raw.replace(",", " ").split()
        numbers = [float(x) for x in parts]
    except ValueError:
        return render_template(
            "index.html",
            name="Salman",
            error="Invalid input. Please enter only numbers."
        )

    results = analyze_numbers(numbers)

    return render_template(
        "results.html",
        results=results,
        numbers=numbers
    )

# --- Lecture 7 Commit 3 template route ---
@app.route("/test-weather")
def test_weather():
    times, temperatures = fetch_hourly_temperature(40.7128, -74.0060)
    return render_template(
        "weather_analysis_results.html",
        times=times,
        temperatures=temperatures
    )

@app.route("/analyze-weather")
def analyze_weather():
    times, temperatures = fetch_hourly_temperature(40.7128, -74.0060)
    results = analyze_time_series(times, temperatures)

    # Temporary test output (JSON) to verify stats
    return jsonify(results=results)

if __name__ == "__main__":
    app.run(debug=True)
