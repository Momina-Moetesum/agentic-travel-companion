# backend/main.py
from fastapi import FastAPI, Request
from backend.agents import create_travel_agent
from backend.tools.sms import send_emergency_sms

app = FastAPI()
agent = create_travel_agent()

@app.post("/plan-trip/")
async def plan_trip(request: Request):
    """
    Endpoint to plan a trip using travel agent.
    """
    user_input = await request.json()
    return agent(user_input)

@app.post("/emergency/")
async def emergency_alert(request: Request):
    """
    Handle POST requests to send an emergency SMS alert.

    Args:
        request (Request): HTTP request with JSON body.

    Returns:
        dict: Message send confirmation.
    """
    data = await request.json()
    result = send_emergency_sms(data["msg"])
    return {"status": result}