# backend/agents.py
from langchain.agents import tool
from backend.tools.weather import get_weather
from backend.tools.sms import send_emergency_sms

@tool
def weather_tool(location: str) -> str:
    """Tool wrapper for weather API."""
    return get_weather(location)

@tool
def emergency_tool(message: str) -> str:
    """Tool wrapper for Twilio emergency SMS."""
    return send_emergency_sms(message)

def create_travel_agent():
    """
    Simulate a travel agent with weather info.

    Returns:
        function: callable agent
    """
    def agent(input: dict):
        return {
            "trip_plan": f"Plan a trip to {input['destination']} with interests: {input['interests']} and budget ${input['budget']}",
            "weather": get_weather(input['destination'])
        }
    return agent