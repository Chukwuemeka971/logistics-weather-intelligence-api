# =========================================================
# SkyRide Logistics Weather Intelligence API
# ---------------------------------------------------------
# Backend weather intelligence service built with FastAPI.
#
# This application integrates:
# 1. Geoapify Geocoding API
# 2. OpenWeatherMap API
#
# The API helps logistics operations retrieve real-time
# weather information for smarter delivery planning,
# route optimization, and operational visibility.
# =========================================================

# -----------------------------
# Import Libraries
# -----------------------------

import os
import requests

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# -----------------------------
# Initialize FastAPI Application
# -----------------------------

app = FastAPI(
    title="SkyRide Logistics Weather API",
    description="Weather intelligence API for logistics operations",
    version="1.0.0"
)


# -----------------------------
# Enable CORS Middleware
# -----------------------------
# Allows frontend applications
# to communicate with the backend.

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------
# Load Environment Variables
# -----------------------------

load_dotenv()

geo_api_key = os.getenv("GEOCODING_API_KEY")
weather_api_key = os.getenv("OPENWEATHER_API_KEY")


# =========================================================
# Helper Functions
# =========================================================

def convert_kelvin_to_celsius(value: float):
    """
    Convert temperature from Kelvin to Celsius.
    """

    return round(value - 273.15, 1)


# =========================================================
# Geocoding Function
# =========================================================

def convert_cityname_to_coordinate(city: str):
    """
    Convert a city name into latitude and longitude
    using the Geoapify Geocoding API.
    """

    url = (
        f"https://api.geoapify.com/v1/geocode/search?"
        f"text={city}&format=json&apiKey={geo_api_key}"
    )

    response = requests.get(url)

    data = response.json()

    # Handle invalid city names
    if not data.get("results"):
        return None, None

    lon = data["results"][0]["lon"]
    lat = data["results"][0]["lat"]

    return lat, lon


# =========================================================
# Weather API Function
# =========================================================

def weather_info(lat: float, lon: float):
    """
    Fetch weather information from OpenWeatherMap API
    using latitude and longitude coordinates.
    """

    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"lat={lat}&lon={lon}&appid={weather_api_key}"
    )

    response = requests.get(url)

    data = response.json()

    return data


# =========================================================
# Weather Response Formatter
# =========================================================

def formatter(payload: dict):
    """
    Format raw weather API response into a clean,
    structured JSON response.
    """

    weather = payload.get("weather", [{}])[0]
    main = payload.get("main", {})
    wind = payload.get("wind", {})

    return {

        "city": payload.get("name"),

        "country": payload.get("sys", {}).get("country"),

        "coordinates": payload.get("coord"),

        "conditions": {
            "label": weather.get("main"),
            "description": weather.get("description"),
            "icon": weather.get("icon"),
        },

        "temperature": {
            "current_c": convert_kelvin_to_celsius(
                main.get("temp", 0)
            ),

            "feels_like_c": convert_kelvin_to_celsius(
                main.get("feels_like", 0)
            ),

            "min_c": convert_kelvin_to_celsius(
                main.get("temp_min", 0)
            ),

            "max_c": convert_kelvin_to_celsius(
                main.get("temp_max", 0)
            ),
        },

        "humidity": main.get("humidity"),

        "pressure": main.get("pressure"),

        "wind": {
            "speed_mps": wind.get("speed"),
            "direction_deg": wind.get("deg"),
            "gust_mps": wind.get("gust"),
        },

        "visibility_m": payload.get("visibility"),

        "cloud_cover_pct": payload.get("clouds", {}).get("all"),

        "timestamp": payload.get("dt"),

        "timezone_offset_s": payload.get("timezone"),

        "source": "OpenWeatherMap"
    }


# =========================================================
# API Routes
# =========================================================

@app.get("/")
def root():
    """
    Root endpoint used to confirm API availability.
    """

    return {
        "message": "SkyRide Logistics Weather API is running"
    }


@app.get("/coordinates")
def coordinates(city: str):
    """
    Retrieve geographic coordinates for a city.
    """

    lat, lon = convert_cityname_to_coordinate(city)

    if lat is None or lon is None:
        return {
            "error": "City not found"
        }

    return {
        "city": city,
        "latitude": lat,
        "longitude": lon
    }


@app.get("/weather")
def weather(city: str):
    """
    Retrieve formatted weather information for a city.
    """

    # Convert city to coordinates
    lat, lon = convert_cityname_to_coordinate(city)

    if lat is None or lon is None:
        return {
            "error": "City not found"
        }

    # Get raw weather data
    payload = weather_info(lat, lon)

    # Format response
    formatted_data = formatter(payload)

    # Add user input city
    formatted_data["input_city"] = city

    return formatted_data


# =========================================================
# Run Application
# =========================================================

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )