import json
import textwrap
import os

import requests
import streamlit as st


# ============================================================
# Configuration
# ============================================================



API_BASE_URL = os.getenv(
    "CAREERPILOT_API_URL",
    "http://127.0.0.1:8000"
)


# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# Custom Styling
# ============================================================

st.markdown(
    """
    <style>

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }

    section[data-testid="stSidebar"] {
        border-right: 1px solid rgba(128, 128, 128, 0.20);
    }

    section[data-testid="stSidebar"] .block-container {
        padding-top: 2rem;
    }

    .brand-title {
        font-size: 28px;
        font-weight: 700;
        margin-bottom: 0;
    }

    .brand-subtitle {
        font-size: 13px;
        opacity: 0.65;
        margin-top: 2px;
        margin-bottom: 25px;
    }

    .hero {
        padding: 32px;
        border-radius: 18px;
        border: 1px solid rgba(128, 128, 128, 0.18);
        margin-bottom: 28px;
    }

    .hero-title {
        font-size: 38px;
        font-weight: 750;
        margin-bottom: 10px;
    }

    .hero-text {
        font-size: 17px;
        opacity: 0.72;
        line-height: 1.6;
        max-width: 850px;
    }

    .section-title {
        font-size: 27px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .section-description {
        opacity: 0.65;
        margin-bottom: 25px;
    }

    .feature-card {
        padding: 22px;
        border-radius: 16px;
        border: 1px solid rgba(128, 128, 128, 0.18);
        min-height: 155px;
        margin-bottom: 12px;
    }

    .feature-icon {
        font-size: 28px;
        margin-bottom: 8px;
    }

    .feature-title {
        font-size: 18px;
        font-weight: 650;
        margin-bottom: 7px;
    }

    .feature-text {
        font-size: 14px;
        opacity: 0.68;
        line-height: 1.5;
    }

    .roadmap-card {
        padding: 18px;
        border-radius: 14px;
        border: 1px solid rgba(128, 128, 128, 0.18);
        margin-bottom: 12px;
    }

    .roadmap-month {
        font-size: 13px;
        font-weight: 700;
        text-transform: uppercase;
        opacity: 0.65;
    }

    .roadmap-goal {
        font-size: 17px;
        font-weight: 600;
        margin-top: 5px;
    }

    .project-card {
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(128, 128, 128, 0.18);
        margin-bottom: 12px;
        min-height: 100px;
    }

    .project-title {
        font-size: 17px;
        font-weight: 650;
        line-height: 1.5;
    }

    .stButton > button {
        border-radius: 10px;
        font-weight: 600;
        min-height: 42px;
    }

    textarea {
        border-radius: 10px !important;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# Helper Functions
# ============================================================

def render_html(content):
    """
    Render custom HTML reliably in Streamlit.
    """

    html = textwrap.dedent(content).strip()

    html = " ".join(
        line.strip()
        for line in html.splitlines()
        if line.strip()
    )

    st.markdown(
        html,
        unsafe_allow_html=True
    )


def parse_result(result):
    """
    Convert JSON strings returned by the backend
    into Python objects.
    """

    if isinstance(result, (dict, list)):
        return result

    if isinstance(result, str):

        try:
            return json.loads(result)

        except (json.JSONDecodeError, TypeError):
            return result

    return result


def api_get(endpoint):
    """
    Send GET request to backend.
    """

    return requests.get(
        f"{API_BASE_URL}{endpoint}",
        timeout=10
    )


def api_post(endpoint, payload):
    """
    Send POST request to backend.
    """

    return requests.post(
        f"{API_BASE_URL}{endpoint}",
        json=payload,
        timeout=120
    )


def show_memory_context(memory_context):
    """
    Display conversation memory when available.
    """

    if memory_context:

        with st.expander(
            "🧠 Conversation Memory",
            expanded=False
        ):

            st.text(memory_context)


def show_api_error(response):
    """
    Display backend errors consistently.
    """

    try:

        data = response.json()

        st.error(
            data.get(
                "message",
                f"Backend returned status code {response.status_code}"
            )
        )

    except Exception:

        st.error(
            f"Backend returned status code {response.status_code}"
        )


# ============================================================
# Navigation State
# ============================================================

pages = [
    "🏠 Dashboard",
    "📄 Resume",
    "🎯 Career",
    "📚 Learning",
    "💡 Projects",
    "🎤 Interview",
    "🔎 Research"
]


if "current_page" not in st.session_state:

    st.session_state.current_page = "🏠 Dashboard"


# ============================================================
# Sidebar
# ============================================================

with st.sidebar:

    render_html(
        """
        <div class="brand-title">
            🚀 CareerPilot AI
        </div>

        <div class="brand-subtitle">
            AI Career & Research Assistant
        </div>
        """
    )

    st.divider()

    navigation = st.radio(
        "Navigation",
        pages,
        index=pages.index(
            st.session_state.current_page
        )
    )

    if navigation != st.session_state.current_page:

        st.session_state.current_page = navigation

        st.rerun()

    st.divider()

    st.markdown("### System")

    if st.button(
        "🔄 Check Backend",
        use_container_width=True
    ):

        try:

            response = api_get("/")

            if response.status_code == 200:

                st.success("🟢 Backend Online")

            else:

                st.warning(
                    f"🟡 Backend: {response.status_code}"
                )

        except requests.exceptions.RequestException:

            st.error("🔴 Backend Offline")

    st.caption("CareerPilot AI")
    st.caption("Student Career Intelligence Platform")


# ============================================================
# DASHBOARD
# ============================================================

if st.session_state.current_page == "🏠 Dashboard":

    render_html(
        """
        <div class="hero">

            <div class="hero-title">
                Your Career. Powered by AI. 🚀
            </div>

            <div class="hero-text">
                CareerPilot AI helps students understand their
                current profile, discover career opportunities,
                build the right skills, create meaningful projects,
                and prepare for interviews.
            </div>

        </div>
        """
    )

    # --------------------------------------------------------
    # Career Command Center
    # --------------------------------------------------------

    render_html(
        """
        <div class="section-title">
            Your Career Command Center
        </div>

        <div class="section-description">
            Start anywhere in your career journey. CareerPilot AI
            will help you plan the next step.
        </div>
        """
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        render_html(
            """
            <div class="feature-card">

                <div class="feature-icon">
                    🧭
                </div>

                <div class="feature-title">
                    Discover
                </div>

                <div class="feature-text">
                    Understand your current skills, education,
                    experience and career direction.
                </div>

            </div>
            """
        )

        if st.button(
            "Open Resume →",
            key="command_resume",
            use_container_width=True
        ):

            st.session_state.current_page = "📄 Resume"
            st.rerun()

    with col2:

        render_html(
            """
            <div class="feature-card">

                <div class="feature-icon">
                    🎯
                </div>

                <div class="feature-title">
                    Plan
                </div>

                <div class="feature-text">
                    Build a personalised roadmap based on
                    your target career.
                </div>

            </div>
            """
        )

        if st.button(
            "Open Career →",
            key="command_career",
            use_container_width=True
        ):

            st.session_state.current_page = "🎯 Career"
            st.rerun()

    with col3:

        render_html(
            """
            <div class="feature-card">

                <div class="feature-icon">
                    🛠️
                </div>

                <div class="feature-title">
                    Build
                </div>

                <div class="feature-text">
                    Learn relevant skills and create projects
                    that strengthen your portfolio.
                </div>

            </div>
            """
        )

        if st.button(
            "Open Projects →",
            key="command_projects",
            use_container_width=True
        ):

            st.session_state.current_page = "💡 Projects"
            st.rerun()

    with col4:

        render_html(
            """
            <div class="feature-card">

                <div class="feature-icon">
                    🎤
                </div>

                <div class="feature-title">
                    Prepare
                </div>

                <div class="feature-text">
                    Practise technical and HR questions
                    personalised to your profile.
                </div>

            </div>
            """
        )

        if st.button(
            "Open Interview →",
            key="command_interview",
            use_container_width=True
        ):

            st.session_state.current_page = "🎤 Interview"
            st.rerun()

    st.divider()

    # --------------------------------------------------------
    # Career Intelligence
    # --------------------------------------------------------

    render_html(
        """
        <div class="section-title">
            Career Intelligence
        </div>

        <div class="section-description">
            Explore the AI capabilities available in CareerPilot.
        </div>
        """
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        render_html(
            """
            <div class="feature-card">

                <div class="feature-icon">
                    📄
                </div>

                <div class="feature-title">
                    Resume Intelligence
                </div>

                <div class="feature-text">
                    Analyse your resume and understand your
                    professional profile.
                </div>

            </div>
            """
        )

        if st.button(
            "Analyse Resume →",
            key="resume_card",
            use_container_width=True
        ):

            st.session_state.current_page = "📄 Resume"
            st.rerun()

    with col2:

        render_html(
            """
            <div class="feature-card">

                <div class="feature-icon">
                    🎯
                </div>

                <div class="feature-title">
                    Career Roadmap
                </div>

                <div class="feature-text">
                    Transform your career goal into a structured
                    roadmap with skills and milestones.
                </div>

            </div>
            """
        )

        if st.button(
            "Build Roadmap →",
            key="career_card",
            use_container_width=True
        ):

            st.session_state.current_page = "🎯 Career"
            st.rerun()

    with col3:

        render_html(
            """
            <div class="feature-card">

                <div class="feature-icon">
                    📚
                </div>

                <div class="feature-title">
                    Learning Intelligence
                </div>

                <div class="feature-text">
                    Create a personalised learning path with
                    courses, books and certifications.
                </div>

            </div>
            """
        )

        if st.button(
            "Create Learning Plan →",
            key="learning_card",
            use_container_width=True
        ):

            st.session_state.current_page = "📚 Learning"
            st.rerun()

    col4, col5, col6 = st.columns(3)

    with col4:

        render_html(
            """
            <div class="feature-card">

                <div class="feature-icon">
                    💡
                </div>

                <div class="feature-title">
                    Project Intelligence
                </div>

                <div class="feature-text">
                    Find portfolio projects aligned with your
                    skills and target career.
                </div>

            </div>
            """
        )

        if st.button(
            "Find Projects →",
            key="project_card",
            use_container_width=True
        ):

            st.session_state.current_page = "💡 Projects"
            st.rerun()

    with col5:

        render_html(
            """
            <div class="feature-card">

                <div class="feature-icon">
                    🎤
                </div>

                <div class="feature-title">
                    Interview Intelligence
                </div>

                <div class="feature-text">
                    Prepare for Python, SQL, ML, LLM,
                    technical and HR questions.
                </div>

            </div>
            """
        )

        if st.button(
            "Start Interview Prep →",
            key="interview_card",
            use_container_width=True
        ):

            st.session_state.current_page = "🎤 Interview"
            st.rerun()

    with col6:

        render_html(
            """
            <div class="feature-card">

                <div class="feature-icon">
                    🔎
                </div>

                <div class="feature-title">
                    AI Research Assistant
                </div>

                <div class="feature-text">
                    Explore career and AI questions through
                    CareerPilot's research pipeline.
                </div>

            </div>
            """
        )

        if st.button(
            "Ask Research →",
            key="research_card",
            use_container_width=True
        ):

            st.session_state.current_page = "🔎 Research"
            st.rerun()

    st.divider()

    # --------------------------------------------------------
    # Career Journey
    # --------------------------------------------------------

    render_html(
        """
        <div class="section-title">
            Your AI Career Journey
        </div>

        <div class="section-description">
            From understanding your profile to becoming
            interview-ready.
        </div>
        """
    )

    step1, step2, step3, step4 = st.columns(4)

    with step1:

        st.markdown("### 01")
        st.markdown("**Understand**")
        st.caption(
            "Analyse your resume, skills and current profile."
        )

    with step2:

        st.markdown("### 02")
        st.markdown("**Plan**")
        st.caption(
            "Define your target career and roadmap."
        )

    with step3:

        st.markdown("### 03")
        st.markdown("**Build**")
        st.caption(
            "Learn skills and develop relevant projects."
        )

    with step4:

        st.markdown("### 04")
        st.markdown("**Prepare**")
        st.caption(
            "Practise interviews and prepare for opportunities."
        )

    st.divider()

    # --------------------------------------------------------
    # Getting Started
    # --------------------------------------------------------

    render_html(
        """
        <div class="section-title">
            🚀 Start Your Career Journey
        </div>

        <div class="section-description">
            Begin with your resume and let CareerPilot AI
            guide your next steps.
        </div>
        """
    )

    start1, start2, start3 = st.columns(3)

    with start1:

        st.markdown("### 📄 Step 1")
        st.markdown("**Analyse your resume**")
        st.caption(
            "Upload your PDF resume to understand your profile."
        )

    with start2:

        st.markdown("### 🎯 Step 2")
        st.markdown("**Create your roadmap**")
        st.caption(
            "Tell CareerPilot what career you want to pursue."
        )

    with start3:

        st.markdown("### 💡 Step 3")
        st.markdown("**Build your portfolio**")
        st.caption(
            "Generate projects and learning recommendations."
        )


# ============================================================
# RESUME
# ============================================================

elif st.session_state.current_page == "📄 Resume":

    render_html(
        """
        <div class="section-title">
            📄 Resume Intelligence
        </div>

        <div class="section-description">
            Upload your resume and let CareerPilot AI understand
            your professional profile.
        </div>
        """
    )

    uploaded_file = st.file_uploader(
        "Upload your resume",
        type=["pdf"],
        help="Upload your resume as a PDF file."
    )

    if uploaded_file is not None:

        st.info(
            f"Selected resume: **{uploaded_file.name}**"
        )

        if st.button(
            "🚀 Analyse Resume",
            use_container_width=True
        ):

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

                        st.success(
                            "Resume analysed successfully!"
                        )

                        resume = parse_result(
                            result.get(
                                "resume_analysis",
                                {}
                            )
                        )

                        if isinstance(resume, dict):

                            skills = resume.get(
                                "skills",
                                []
                            )

                            education = resume.get(
                                "education",
                                []
                            )

                            experience = resume.get(
                                "experience",
                                []
                            )

                            projects = resume.get(
                                "projects",
                                []
                            )

                            certifications = resume.get(
                                "certifications",
                                []
                            )

                            m1, m2, m3, m4, m5 = st.columns(5)

                            with m1:
                                st.metric(
                                    "Skills",
                                    len(skills)
                                )

                            with m2:
                                st.metric(
                                    "Education",
                                    len(education)
                                )

                            with m3:
                                st.metric(
                                    "Experience",
                                    len(experience)
                                )

                            with m4:
                                st.metric(
                                    "Projects",
                                    len(projects)
                                )

                            with m5:
                                st.metric(
                                    "Certifications",
                                    len(certifications)
                                )

                            st.divider()

                            st.subheader(
                                f"👤 {resume.get('name', 'Candidate')}"
                            )

                            c1, c2 = st.columns(2)

                            with c1:

                                st.markdown("### Contact")

                                if resume.get("email"):
                                    st.write(
                                        f"📧 {resume.get('email')}"
                                    )

                                if resume.get("phone"):
                                    st.write(
                                        f"📱 {resume.get('phone')}"
                                    )

                            with c2:

                                st.markdown("### Skills")

                                if skills:

                                    st.write(
                                        " • ".join(
                                            str(skill)
                                            for skill in skills
                                        )
                                    )

                            with st.expander(
                                "🎓 Education",
                                expanded=True
                            ):

                                for item in education:
                                    st.write(f"• {item}")

                            with st.expander(
                                "💼 Experience"
                            ):

                                for item in experience:
                                    st.write(f"• {item}")

                            with st.expander(
                                "🚀 Projects"
                            ):

                                for item in projects:
                                    st.write(f"• {item}")

                            with st.expander(
                                "🏆 Certifications"
                            ):

                                for item in certifications:
                                    st.write(f"• {item}")

                        else:

                            st.json(resume)

                        show_memory_context(
                            result.get(
                                "memory_context",
                                ""
                            )
                        )

                    else:

                        st.error(
                            result.get(
                                "message",
                                "Resume analysis failed."
                            )
                        )

                else:

                    show_api_error(response)

            except requests.exceptions.RequestException as error:

                st.error(
                    f"Could not connect to backend: {error}"
                )


# ============================================================
# CAREER
# ============================================================

elif st.session_state.current_page == "🎯 Career":

    render_html(
        """
        <div class="section-title">
            🎯 Career Roadmap
        </div>

        <div class="section-description">
            Turn your current skills into a structured career strategy.
        </div>
        """
    )

    career_input = st.text_area(
        "Tell CareerPilot about your career goal",
        placeholder=(
            "Example: I know Python and SQL and want to become "
            "a Data Analyst."
        ),
        height=150
    )

    if st.button(
        "🎯 Generate Career Roadmap",
        use_container_width=True
    ):

        if not career_input.strip():

            st.warning(
                "Please enter your career information."
            )

        else:

            try:

                response = api_post(
                    "/career/roadmap",
                    {
                        "career_goal": career_input
                    }
                )

                if response.status_code == 200:

                    result = response.json()

                    if result.get("success"):

                        st.success(
                            "Career roadmap generated!"
                        )

                        career = parse_result(
                            result.get("result")
                        )

                        if isinstance(career, dict):

                            c1, c2 = st.columns(2)

                            with c1:

                                st.markdown(
                                    "### 🎯 Career Goal"
                                )

                                st.info(
                                    career.get(
                                        "career_goal",
                                        "Not specified"
                                    )
                                )

                            with c2:

                                st.markdown(
                                    "### 📈 Current Level"
                                )

                                st.info(
                                    career.get(
                                        "current_level",
                                        "Not specified"
                                    )
                                )

                            st.divider()

                            missing_skills = career.get(
                                "missing_skills",
                                []
                            )

                            certifications = career.get(
                                "recommended_certifications",
                                []
                            )

                            projects = career.get(
                                "recommended_projects",
                                []
                            )

                            col1, col2, col3 = st.columns(3)

                            with col1:

                                st.markdown(
                                    "### 🧩 Missing Skills"
                                )

                                for item in missing_skills:
                                    st.write(f"• {item}")

                            with col2:

                                st.markdown(
                                    "### 🏆 Certifications"
                                )

                                for item in certifications:
                                    st.write(f"• {item}")

                            with col3:

                                st.markdown(
                                    "### 💡 Projects"
                                )

                                for item in projects:
                                    st.write(f"• {item}")

                            st.divider()

                            st.markdown(
                                "### 🗺️ Your Roadmap"
                            )

                            roadmap = career.get(
                                "roadmap",
                                []
                            )

                            for item in roadmap:

                                if isinstance(item, dict):

                                    render_html(
                                        f"""
                                        <div class="roadmap-card">

                                            <div class="roadmap-month">
                                                Month {item.get('month', '')}
                                            </div>

                                            <div class="roadmap-goal">
                                                {item.get('goal', '')}
                                            </div>

                                        </div>
                                        """
                                    )

                        else:

                            st.write(career)

                        show_memory_context(
                            result.get(
                                "memory_context",
                                ""
                            )
                        )

                    else:

                        st.error(
                            result.get(
                                "message",
                                "Career roadmap generation failed."
                            )
                        )

                else:

                    show_api_error(response)

            except requests.exceptions.RequestException as error:

                st.error(
                    f"Could not connect to backend: {error}"
                )


# ============================================================
# LEARNING
# ============================================================

elif st.session_state.current_page == "📚 Learning":

    render_html(
        """
        <div class="section-title">
            📚 Learning Intelligence
        </div>

        <div class="section-description">
            Build a personalised learning path around your career goal.
        </div>
        """
    )

    learning_input = st.text_area(
        "Enter your career goal or roadmap",
        placeholder=(
            "Example: I want to become a Data Analyst. "
            "I need to improve Python, SQL, Excel and Power BI."
        ),
        height=150
    )

    if st.button(
        "📚 Generate Learning Plan",
        use_container_width=True
    ):

        if not learning_input.strip():

            st.warning(
                "Please enter your career goal or roadmap."
            )

        else:

            try:

                response = api_post(
                    "/learning/plan",
                    {
                        "career_goal": learning_input
                    }
                )

                if response.status_code == 200:

                    result = response.json()

                    if result.get("success"):

                        st.success(
                            "Personalised learning plan generated!"
                        )

                        learning = parse_result(
                            result.get("result")
                        )

                        if isinstance(learning, dict):

                            st.markdown(
                                "### 🛣️ Learning Path"
                            )

                            for item in learning.get(
                                "learning_path",
                                []
                            ):
                                st.write(f"• {item}")

                            st.divider()

                            col1, col2 = st.columns(2)

                            with col1:

                                st.markdown(
                                    "### 🎓 Recommended Courses"
                                )

                                for item in learning.get(
                                    "recommended_courses",
                                    []
                                ):
                                    st.write(f"• {item}")

                                st.markdown(
                                    "### 📚 Recommended Books"
                                )

                                for item in learning.get(
                                    "recommended_books",
                                    []
                                ):
                                    st.write(f"• {item}")

                            with col2:

                                st.markdown(
                                    "### 🏆 Certifications"
                                )

                                for item in learning.get(
                                    "recommended_certifications",
                                    []
                                ):
                                    st.write(f"• {item}")

                                st.markdown(
                                    "### 📅 Weekly Plan"
                                )

                                for item in learning.get(
                                    "weekly_plan",
                                    []
                                ):

                                    if isinstance(item, dict):

                                        st.write(
                                            f"**Week {item.get('week')}** — "
                                            f"{item.get('goal')}"
                                        )

                        else:

                            st.write(learning)

                        show_memory_context(
                            result.get(
                                "memory_context",
                                ""
                            )
                        )

                    else:

                        st.error(
                            result.get(
                                "message",
                                "Learning plan generation failed."
                            )
                        )

                else:

                    show_api_error(response)

            except requests.exceptions.RequestException as error:

                st.error(
                    f"Could not connect to backend: {error}"
                )


# ============================================================
# PROJECTS
# ============================================================

elif st.session_state.current_page == "💡 Projects":

    render_html(
        """
        <div class="section-title">
            💡 Project Intelligence
        </div>

        <div class="section-description">
            Discover portfolio projects that match your skills and goals.
        </div>
        """
    )

    project_input = st.text_area(
        "Enter your skills and career goal",
        placeholder=(
            "Example: I know Python, SQL, Pandas and Power BI. "
            "I want to become a Data Analyst."
        ),
        height=150
    )

    if st.button(
        "💡 Recommend Projects",
        use_container_width=True
    ):

        if not project_input.strip():

            st.warning(
                "Please enter your skills and career goal."
            )

        else:

            try:

                response = api_post(
                    "/project/recommend",
                    {
                        "resume_data": {
                            "skills": project_input
                        },
                        "career_data": {
                            "career_goal": project_input
                        }
                    }
                )

                if response.status_code == 200:

                    result = response.json()

                    if result.get("success"):

                        st.success(
                            "Project recommendations generated!"
                        )

                        projects = parse_result(
                            result.get("result")
                        )

                        if isinstance(projects, dict):

                            levels = [
                                (
                                    "🌱 Beginner Projects",
                                    "beginner_projects"
                                ),
                                (
                                    "🚀 Intermediate Projects",
                                    "intermediate_projects"
                                ),
                                (
                                    "🔥 Advanced Projects",
                                    "advanced_projects"
                                )
                            ]

                            for title, key in levels:

                                st.markdown(
                                    f"### {title}"
                                )

                                items = projects.get(
                                    key,
                                    []
                                )

                                if items:

                                    cols = st.columns(
                                        min(
                                            len(items),
                                            3
                                        )
                                    )

                                    for index, item in enumerate(items):

                                        with cols[
                                            index % len(cols)
                                        ]:

                                            render_html(
                                                f"""
                                                <div class="project-card">

                                                    <div class="project-title">
                                                        {item}
                                                    </div>

                                                </div>
                                                """
                                            )

                                else:

                                    st.caption(
                                        "No recommendations returned."
                                    )

                            st.divider()

                            col1, col2 = st.columns(2)

                            with col1:

                                st.markdown(
                                    "### 🗂️ GitHub Structure"
                                )

                                for item in projects.get(
                                    "recommended_github_structure",
                                    []
                                ):
                                    st.write(f"• {item}")

                            with col2:

                                st.markdown(
                                    "### ☁️ Deployment Suggestions"
                                )

                                for item in projects.get(
                                    "deployment_suggestions",
                                    []
                                ):
                                    st.write(f"• {item}")

                        else:

                            st.write(projects)

                        show_memory_context(
                            result.get(
                                "memory_context",
                                ""
                            )
                        )

                    else:

                        st.error(
                            result.get(
                                "message",
                                "Project recommendation failed."
                            )
                        )

                else:

                    show_api_error(response)

            except requests.exceptions.RequestException as error:

                st.error(
                    f"Could not connect to backend: {error}"
                )


# ============================================================
# INTERVIEW
# ============================================================

elif st.session_state.current_page == "🎤 Interview":

    render_html(
        """
        <div class="section-title">
            🎤 Interview Intelligence
        </div>

        <div class="section-description">
            Prepare for interviews using questions personalised
            to your profile.
        </div>
        """
    )

    interview_input = st.text_area(
        "Enter your resume, career goal and project information",
        placeholder=(
            "Example: I know Python, SQL, Pandas and Power BI. "
            "I want to become a Data Analyst. "
            "My project is a retail sales analytics dashboard."
        ),
        height=170
    )

    if st.button(
        "🎤 Generate Interview Preparation",
        use_container_width=True
    ):

        if not interview_input.strip():

            st.warning(
                "Please enter your interview preparation information."
            )

        else:

            try:

                response = api_post(
                    "/interview/prepare",
                    {
                        "resume_data": {
                            "information": interview_input
                        },
                        "career_data": {
                            "career_goal": interview_input
                        },
                        "learning_data": {
                            "learning_goal": interview_input
                        },
                        "project_data": {
                            "projects": interview_input
                        }
                    }
                )

                if response.status_code == 200:

                    result = response.json()

                    if result.get("success"):

                        st.success(
                            "Interview preparation generated!"
                        )

                        interview = parse_result(
                            result.get("result")
                        )

                        if isinstance(interview, dict):

                            categories = [
                                (
                                    "💻 Technical",
                                    "technical_questions"
                                ),
                                (
                                    "🐍 Python",
                                    "python_questions"
                                ),
                                (
                                    "🗄️ SQL",
                                    "sql_questions"
                                ),
                                (
                                    "🤖 Machine Learning",
                                    "machine_learning_questions"
                                ),
                                (
                                    "🧠 LLM",
                                    "llm_questions"
                                ),
                                (
                                    "👔 HR",
                                    "hr_questions"
                                ),
                                (
                                    "🚀 Projects",
                                    "project_questions"
                                )
                            ]

                            tabs = st.tabs(
                                [
                                    title
                                    for title, key in categories
                                ]
                            )

                            for tab, (
                                title,
                                key
                            ) in zip(
                                tabs,
                                categories
                            ):

                                with tab:

                                    questions = interview.get(
                                        key,
                                        []
                                    )

                                    if questions:

                                        for index, question in enumerate(
                                            questions,
                                            start=1
                                        ):

                                            with st.expander(
                                                f"Question {index}"
                                            ):

                                                st.write(question)

                                    else:

                                        st.caption(
                                            "No questions returned."
                                        )

                            st.divider()

                            st.markdown(
                                "### 📈 Improvement Tips"
                            )

                            for tip in interview.get(
                                "improvement_tips",
                                []
                            ):
                                st.write(f"• {tip}")

                        else:

                            st.write(interview)

                        show_memory_context(
                            result.get(
                                "memory_context",
                                ""
                            )
                        )

                    else:

                        st.error(
                            result.get(
                                "message",
                                "Interview preparation failed."
                            )
                        )

                else:

                    show_api_error(response)

            except requests.exceptions.RequestException as error:

                st.error(
                    f"Could not connect to backend: {error}"
                )


# ============================================================
# RESEARCH
# ============================================================

elif st.session_state.current_page == "🔎 Research":

    render_html(
        """
        <div class="section-title">
            🔎 AI Research Assistant
        </div>

        <div class="section-description">
            Ask career and AI-related questions using CareerPilot AI's
            knowledge-grounded research pipeline.
        </div>
        """
    )

    research_question = st.text_area(
        "What would you like to research?",
        placeholder=(
            "Example: What skills are required to become "
            "an AI Engineer?"
        ),
        height=150
    )

    if st.button(
        "🔎 Ask Research Assistant",
        use_container_width=True
    ):

        if not research_question.strip():

            st.warning(
                "Please enter a research question."
            )

        else:

            try:

                response = api_post(
                    "/research/ask",
                    {
                        "question": research_question
                    }
                )

                if response.status_code == 200:

                    result = response.json()

                    if result.get("success"):

                        research = parse_result(
                            result.get("result")
                        )

                        st.success(
                            "Research answer generated!"
                        )

                        if isinstance(research, dict):

                            question = research.get(
                                "question",
                                research_question
                            )

                            answer = research.get(
                                "answer",
                                ""
                            )

                            st.markdown(
                                "### ❓ Your Question"
                            )

                            st.info(question)

                            st.markdown(
                                "### 🧠 Research Answer"
                            )

                            st.write(answer)

                        else:

                            st.write(research)

                        show_memory_context(
                            result.get(
                                "memory_context",
                                ""
                            )
                        )

                    else:

                        st.error(
                            result.get(
                                "message",
                                "Research request failed."
                            )
                        )

                else:

                    show_api_error(response)

            except requests.exceptions.RequestException as error:

                st.error(
                    f"Could not connect to backend: {error}"
                )