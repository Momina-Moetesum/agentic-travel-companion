# frontend/app.py
import streamlit as st
import requests

st.title("✈️ Travel Companion Agent")

destination = st.text_input("Where do you want to go?")
interests = st.text_area("What are your interests?")
budget = st.slider("Budget", 100, 5000)

if st.button("Plan Trip"):
    response = requests.post("http://localhost:8000/plan-trip/", json={
        "destination": destination,
        "interests": interests,
        "budget": budget
    })
    st.json(response.json())

if st.button("Emergency SOS"):
    message = st.text_input("Emergency Message")
    if message:
        response = requests.post("http://localhost:8000/emergency/", json={"msg": message})
        st.success("Emergency sent!")