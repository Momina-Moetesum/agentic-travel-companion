# backend/tools/sms.py
from twilio.rest import Client
import os

def send_emergency_sms(msg: str) -> str:
    """
    Send an emergency SMS using Twilio.

    Args:
        msg (str): Emergency message content

    Returns:
        str: Confirmation message SID
    """
    account_sid = os.getenv("TWILIO_SID")
    auth_token = os.getenv("TWILIO_TOKEN")
    to = os.getenv("TWILIO_TO")
    sender = os.getenv("TWILIO_FROM")

    client = Client(account_sid, auth_token)
    message = client.messages.create(body=msg, from_=sender, to=to)
    return f"Message sent: {message.sid}"