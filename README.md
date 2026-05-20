# SkyRide Weather Intelligence API

A backend weather intelligence service built with FastAPI to support smarter logistics operations through real-time weather monitoring and API integration.

This project was developed as part of a logistics-focused data engineering case study for SkyRide Logistics Ltd, where weather disruptions were affecting delivery operations, route planning, and customer satisfaction. 

---

## Business Problem

SkyRide Logistics experienced operational challenges caused by sudden weather changes, including:

- Delivery delays due to rainfall and poor visibility
- Inefficient manual weather checks
- Lack of location-specific weather intelligence
- Reduced customer satisfaction from delayed deliveries

The objective of this project was to build a backend weather service capable of providing automated, real-time weather information to support logistics decision-making. 

---

## My Contribution

My contribution focused on backend engineering and API integration.

Responsibilities included:

- Developing the FastAPI backend service
- Integrating Geoapify and OpenWeatherMap APIs
- Building RESTful weather endpoints
- Formatting raw API responses into structured JSON
- Implementing environment variable management
- Enabling frontend-backend communication using CORS middleware
- Integrating backend services with an existing frontend dispatch dashboard

---

## Tech Stack

### Backend
- Python
- FastAPI
- Requests
- Uvicorn
- Python-dotenv

### External APIs
- Geoapify Geocoding API
- OpenWeatherMap API

### Integration
- Frontend dispatch dashboard integration using JavaScript Fetch API

---

## Features

### Backend Features
- Convert city names into geographic coordinates
- Retrieve real-time weather information
- Format raw API responses into structured JSON
- RESTful API endpoints using FastAPI
- Environment variable management with `.env`
- Frontend integration support using CORS middleware
- Error handling for invalid city requests

### Integration Features
- Backend integration with an existing logistics dispatch dashboard
- Real-time weather retrieval via asynchronous API requests
- Structured weather intelligence responses for frontend rendering

---

## API Endpoints

### Root Endpoint

```http
GET /
```

Response:

```json
{
  "message": "SkyRide Logistics Weather API is running"
}
```

---

### Coordinates Endpoint

```http
GET /coordinates?city=london
```

Response:

```json
{
  "city": "london",
  "latitude": 51.5074,
  "longitude": -0.1278
}
```

---

### Weather Endpoint

```http
GET /weather?city=london
```

Response:

```json
{
  "city": "London",
  "country": "GB",
  "conditions": {
    "label": "Clouds",
    "description": "broken clouds"
  },
  "temperature": {
    "current_c": 18.2,
    "feels_like_c": 17.5
  }
}
```

---

## Project Architecture

```text
Frontend Dispatch Dashboard
        ↓
JavaScript Fetch API
        ↓
FastAPI Backend Service
        ↓
Geoapify Geocoding API
        ↓
OpenWeatherMap API
        ↓
Structured Weather Intelligence Response
```

---

## Installation

### Clone Repository

```bash
git clone <https://github.com/Chukwuemeka971/logistics-weather-intelligence-api>
cd logistics-weather-intelligence-api
```

---

### Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root directory:

```env
GEOCODING_API_KEY=your_geoapify_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
```

---

## Run the Application

```bash
uvicorn app:app --reload
```

Application runs on:

```text
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically generates Swagger API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Learning Outcomes

This project strengthened my understanding of:

- REST API development
- Backend application architecture
- Third-party API integration
- Frontend-backend communication
- JSON transformation and formatting
- Environment variable management
- Real-world logistics use cases for weather intelligence

---

## Business Impact

This solution supports logistics operations by enabling:

- Smarter route planning
- Improved delivery scheduling
- Better operational visibility
- Faster weather awareness
- More informed dispatch decisions

---

## Future Improvements

- Async API requests using `httpx`
- Docker containerization
- Cloud deployment
- API response validation with Pydantic
- Weather forecasting support
- Database integration for weather analytics
- Route optimization intelligence
