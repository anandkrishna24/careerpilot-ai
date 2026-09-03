import requests
import streamlit as st

API_BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide"
)

st.title("CareerPilot AI 🚀")

st.markdown(
    """
    ### AI Career & Research Assistant

    CareerPilot AI helps students with:

    - Resume analysis
    - Career roadmaps
    - Personalised learning plans
    - Project recommendations
    - Interview preparation
    - AI career research
    """
)

st.divider()

st.subheader("Backend Connection")

if st.button("Test Backend Connection"):
    try:
        response = requests.get(f"{API_BASE_URL}/")

        if response.status_code == 200:
            st.success("Backend connected successfully!")
            st.json(response.json())
        else:
            st.error(
                f"Backend returned status code: {response.status_code}"
            )

    except requests.exceptions.RequestException as error:
        st.error(f"Could not connect to backend: {error}")