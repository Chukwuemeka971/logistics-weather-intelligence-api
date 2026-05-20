# SkyRide Logistics Weather Intelligence API

A backend weather intelligence service built with FastAPI that helps logistics companies make smarter operational decisions using real-time weather data.

This project was developed as a data engineering and API integration case study for SkyRide Logistics Ltd, a logistics company facing delivery delays caused by sudden weather changes and poor visibility. 

---

## Business Problem

SkyRide Logistics experienced:

- Delivery delays caused by heavy rainfall and poor visibility
- Customer dissatisfaction from inaccurate delivery expectations
- Inefficient manual weather checks
- Lack of location-specific weather insights for dispatch planning

To address this, the project integrates external weather APIs into a web application backend to provide automated, real-time weather updates for operational decision-making. 

---

## Project Objectives

This project demonstrates how APIs can support business operations through:

- Real-time weather intelligence
- API integration and data retrieval
- Backend service development
- Structured JSON response formatting
- Frontend-backend communication
- Operational optimization for logistics workflows

---

## Tech Stack

### Backend
- FastAPI
- Python
- Requests
- Uvicorn
- Python-dotenv

### APIs
- OpenWeatherMap API
- Geoapify Geocoding API

### Frontend
- Integrated with frontend weather dashboard application

---

## Features

- Convert city names into geographic coordinates
- Retrieve real-time weather information
- Format raw API responses into clean structured JSON
- RESTful API endpoints
- Frontend integration support with CORS middleware
- Environment variable management using `.env`

---

## API Endpoints

### Root Endpoint

```http
GET /
```

Response:

```json
{
  "message": "Weather API is running"
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
Frontend Application
        ↓
FastAPI Backend
        ↓
Geoapify API (Coordinates)
        ↓
OpenWeatherMap API (Weather Data)
        ↓
Structured JSON Response
```

---

## Installation

### Clone Repository

```bash
git clone <your-repository-url>
cd weather-api-project
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

Create a `.env` file in the project root:

```env
GEOCODING_API_KEY=your_geoapify_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
```

---

## Run the Application

```bash
uvicorn app:app --reload
```

Server runs on:

```text
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically generates Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Learning Outcomes

This project strengthened my understanding of:

- REST API development
- API integration workflows
- Backend application architecture
- JSON transformation and formatting
- Environment variable management
- Frontend-backend integration
- Real-world logistics use cases for weather intelligence

---

## Business Impact

This solution helps logistics operations improve:

- Route planning efficiency
- Delivery scheduling
- Operational visibility
- Customer communication
- Risk reduction during adverse weather conditions

---

## Future Improvements

- Add async API requests
- Docker containerization
- Deployment to cloud platforms
- API response validation with Pydantic
- Weather forecasting support
- Database integration for historical weather analytics
- Route optimization intelligence

---

## Author

Chukwuemeka Nwankwo

Aspiring Data Engineer | Backend API Development | Python | FastAPI

