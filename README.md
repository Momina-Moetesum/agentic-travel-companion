# Agentic Travel Companion

An agentic AI application that helps users plan trips and send emergency alerts using LangGraph, Streamlit, and FastAPI.

---

## What It Does

- Plans trips based on destination, interests, and budget
- Fetches real-time weather using OpenWeather API
- Sends emergency SMS alerts via Twilio
- Uses LangGraph (LangChain) agents and tools

---

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: FastAPI
- **Agent Layer**: LangGraph / LangChain
- **APIs**: OpenWeatherMap, Twilio
- **Observability**: Logging + optional LangSmith or LangFuse

---

## Project Structure
.
├── backend/
│   ├── main.py          # FastAPI backend
│   ├── agents.py        # LangGraph agent setup
│   └── tools/
│       ├── weather.py   # Weather API
│       └── sms.py       # Twilio
├── frontend/
│   └── app.py           # Streamlit app
├── Dockerfile
├── docker-compose.yml
├── .env
├── .gitignore
├── README.md

