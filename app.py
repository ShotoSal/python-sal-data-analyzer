from flask import Flask, render_template, request, jsonify
from analyzer import analyze_numbers
from external_api import fetch_hourly_temperature
from weather_analysis import analyze_time_series

app = Flask(__name__)

# -------------------------------
# Home page
# -------------------------------
@app.route("/", methods=["GET"])
def index():
    name = "Salman"
    return render_template("index.html", name=name)

# -------------------------------
# Number analyzer (existing)
# -------------------------------
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

# -------------------------------
# Commit #6: Weather input page
# -------------------------------
@app.route("/weather-input")
def weather_input():
    return render_template("weather_input.html")

# -------------------------------
# Commit #6: Analyze weather (POST)
# -------------------------------
@app.route("/analyze-weather", methods=["POST"])
def analyze_weather():
    try:
        lat = float(request.form.get("lat"))
        lon = float(request.form.get("lon"))
    except (TypeError, ValueError):
        return render_template(
            "weather_input.html",
            error="Invalid latitude or longitude. Please enter numeric values."
        )

    times, temperatures = fetch_hourly_temperature(lat, lon)
    analysis = analyze_time_series(times, temperatures)

    return render_template(
        "weather_analysis_results.html",
        times=times,
        temperatures=temperatures,
        analysis=analysis,
        location_name="Custom Location",
        lat=lat,
        lon=lon
    )

# -------------------------------
# Optional JSON debug endpoint
# -------------------------------
@app.route("/analyze-weather.json")
def analyze_weather_json():
    times, temperatures = fetch_hourly_temperature(40.7128, -74.0060)
    analysis = analyze_time_series(times, temperatures)
    return jsonify(
        count=analysis["count"],
        min=analysis["min"],
        max=analysis["max"],
        mean=analysis["mean"],
        median=analysis["median"],
        std_dev=analysis["std_dev"]
    )

# -------------------------------
# Run app
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True, port=5001)
