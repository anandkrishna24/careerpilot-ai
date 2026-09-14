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

# Backend connection
st.subheader("Backend Connection")

if st.button("Test Backend Connection"):
    try:
        response = requests.get(
            f"{API_BASE_URL}/",
            timeout=5
        )

        if response.status_code == 200:
            st.success("Backend connected successfully!")
            st.json(response.json())
        else:
            st.error(
                f"Backend returned status code: {response.status_code}"
            )

    except requests.exceptions.RequestException as error:
        st.error(f"Could not connect to backend: {error}")

st.divider()

# System status
st.subheader("System Status")

if st.button("Check System Status"):
    try:
        response = requests.get(
            f"{API_BASE_URL}/",
            timeout=5
        )

        if response.status_code == 200:
            st.success("🟢 CareerPilot AI backend is online.")
        else:
            st.warning(
                f"🟡 Backend responded with status code "
                f"{response.status_code}."
            )

    except requests.exceptions.RequestException:
        st.error("🔴 CareerPilot AI backend is offline.")

st.divider()

# Resume upload
st.subheader("Resume Analysis")

uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["pdf"],
    help="Upload your resume as a PDF file."
)

if uploaded_file is not None:
    st.write(f"Selected file: **{uploaded_file.name}**")

    if st.button("Analyze Resume"):
        try:
            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    "application/pdf"
                )
            }

            response = requests.post(
                f"{API_BASE_URL}/resume/upload",
                files=files,
                timeout=120
            )

            if response.status_code == 200:
                result = response.json()

                if result.get("success"):
                    st.success("Resume uploaded and analyzed successfully!")

                    st.subheader("Resume Analysis")
                    st.json(result.get("resume_analysis"))

                    if result.get("memory_context"):
                        with st.expander("Memory Context"):
                            st.text(result["memory_context"])

                else:
                    st.error(
                        result.get(
                            "message",
                            "Resume analysis failed."
                        )
                    )

            else:
                st.error(
                    f"Backend returned status code: {response.status_code}"
                )

        except requests.exceptions.RequestException as error:
            st.error(f"Could not connect to backend: {error}")

st.divider()

# Career roadmap
st.subheader("Career Roadmap")

career_input = st.text_area(
    "Enter your career information",
    placeholder=(
        "Example: I know Python and SQL and want to become "
        "a Data Analyst."
    ),
    height=120
)

if st.button("Generate Career Roadmap"):
    if not career_input.strip():
        st.warning("Please enter your career information.")
    else:
        try:
            response = requests.post(
                f"{API_BASE_URL}/career/roadmap",
                json={
                    "career_goal": career_input
                },
                timeout=120
            )

            if response.status_code == 200:
                result = response.json()

                if result.get("success"):
                    st.success("Career roadmap generated successfully!")

                    st.subheader("Career Roadmap")
                    st.json(result.get("result"))

                    if result.get("memory_context"):
                        with st.expander("Memory Context"):
                            st.text(result["memory_context"])
                else:
                    st.error(
                        result.get(
                            "message",
                            "Career roadmap generation failed."
                        )
                    )
            else:
                st.error(
                    f"Backend returned status code: "
                    f"{response.status_code}"
                )

        except requests.exceptions.RequestException as error:
            st.error(f"Could not connect to backend: {error}")


st.divider()

# Learning plan
st.subheader("Personalised Learning Plan")

learning_input = st.text_area(
    "Enter your career goal or roadmap",
    placeholder=(
        "Example: I want to become a Data Analyst. "
        "I need to improve Python, SQL, Excel, and Power BI."
    ),
    height=120
)

if st.button("Generate Learning Plan"):
    if not learning_input.strip():
        st.warning("Please enter your career goal or roadmap.")
    else:
        try:
            response = requests.post(
                f"{API_BASE_URL}/learning/plan",
                json={
                    "career_goal": learning_input
                },
                timeout=120
            )

            if response.status_code == 200:
                result = response.json()

                if result.get("success"):
                    st.success(
                        "Personalised learning plan generated successfully!"
                    )

                    st.subheader("Learning Plan")
                    st.json(result.get("result"))

                    if result.get("memory_context"):
                        with st.expander("Memory Context"):
                            st.text(result["memory_context"])
                else:
                    st.error(
                        result.get(
                            "message",
                            "Learning plan generation failed."
                        )
                    )

            else:
                st.error(
                    f"Backend returned status code: "
                    f"{response.status_code}"
                )

        except requests.exceptions.RequestException as error:
            st.error(f"Could not connect to backend: {error}")