import streamlit as st


st.set_page_config(
    page_title="About | SkyReveal",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# TOP NAVIGATION

logo_col, home_col, analyze_col, learn_col, about_col = st.columns(
    [4, 1, 1, 1, 1]
)

with logo_col:
    st.markdown("### 🌌 SkyReveal")

with home_col:
    st.page_link("app.py", label="Home")

with analyze_col:
    st.page_link("pages/1_Analyze.py", label="Analyze")

with learn_col:
    st.page_link("pages/2_Learn.py", label="Learn")

with about_col:
    st.page_link("pages/3_About.py", label="About")

st.divider()

# HERO

hero_text, hero_stat = st.columns([2, 1], gap="large")

with hero_text:
    st.caption("ABOUT THE PROJECT")

    st.title("Making light pollution visible.")

    st.write(
        """
        SkyReveal is an open-source awareness platform that uses computer
        vision to help people understand how artificial lighting changes
        their view of the night sky.
        """
    )

with hero_stat:
    with st.container(border=True):
        st.metric(
            label="Project Version",
            value="1.0"
        )

        st.write("Built as an accessible educational tool.")

st.divider()

# MISSION

mission_col, purpose_col = st.columns(2, gap="large")

with mission_col:
    with st.container(border=True):
        st.subheader("The Problem")

        st.write(
            """
            Artificial lighting brightens the night sky and makes faint stars,
            constellations, and the Milky Way harder to see.

            Light pollution can also affect wildlife, waste energy, and
            interfere with astronomical observation.
            """
        )

with purpose_col:
    with st.container(border=True):
        st.subheader("The Mission")

        st.write(
            """
            SkyReveal aims to reconnect people with the night sky by making
            light pollution easier to understand through accessible technology,
            visual analysis, and education.
            """
        )

# WHY IT WAS BUILT

st.subheader("Why SkyReveal Was Built")

st.write(
    """
    Light pollution is often difficult to notice because it gradually becomes
    part of everyday life. SkyReveal was created to turn an ordinary night-sky
    photograph into a clear and understandable report.

    Rather than simply producing a number, the platform explains what may be
    affecting the sky and what the user could potentially see under darker
    conditions.
    """
)

st.divider()

# HOW IT WORKS

st.subheader("How It Works")

step1, step2, step3, step4 = st.columns(4, gap="medium")

with step1:
    with st.container(border=True):
        st.markdown("### 01")
        st.markdown("**Upload**")
        st.write("The user uploads a photograph of the night sky.")

with step2:
    with st.container(border=True):
        st.markdown("### 02")
        st.markdown("**Detect**")
        st.write("Computer vision identifies bright star-like objects.")

with step3:
    with st.container(border=True):
        st.markdown("### 03")
        st.markdown("**Measure**")
        st.write("The image is analyzed for darkness, contrast, and clouds.")

with step4:
    with st.container(border=True):
        st.markdown("### 04")
        st.markdown("**Explain**")
        st.write("SkyReveal generates an educational sky-quality report.")

st.divider()

# TECHNOLOGY

st.subheader("Technology Behind SkyReveal")

python_col, streamlit_col, opencv_col, data_col = st.columns(4)

with python_col:
    with st.container(border=True):
        st.markdown("### 🐍")
        st.markdown("**Python**")
        st.caption("Core application logic")

with streamlit_col:
    with st.container(border=True):
        st.markdown("### 🌐")
        st.markdown("**Streamlit**")
        st.caption("Interactive web interface")

with opencv_col:
    with st.container(border=True):
        st.markdown("### 👁️")
        st.markdown("**OpenCV**")
        st.caption("Image and star detection")

with data_col:
    with st.container(border=True):
        st.markdown("### 📊")
        st.markdown("**NumPy & Pillow**")
        st.caption("Image data processing")

# LIMITATIONS AND ROADMAP

st.divider()

limitations_col, roadmap_col = st.columns(2, gap="large")

with limitations_col:
    st.subheader("Current Limitations")

    with st.container(border=True):
        st.write(
            """
            SkyReveal is an educational tool rather than a scientific instrument.

            Results may be influenced by:

            - camera exposure and night mode
            - image editing
            - moonlight
            - clouds and haze
            - nearby artificial lights
            - buildings and other foreground objects
            """
        )

with roadmap_col:
    st.subheader("Future Development")

    with st.container(border=True):
        st.write(
            """
            Planned improvements include:

            - sky-region segmentation
            - improved cloud detection
            - shareable result cards
            - Bortle Scale comparisons
            - location-aware recommendations
            - community sky submissions
            """
        )

# CALL TO ACTION

st.divider()

cta_text, cta_button = st.columns([3, 1])

with cta_text:
    st.subheader("Ready to explore your night sky?")
    st.write("Upload a photograph and generate your SkyReveal report.")

with cta_button:
    st.page_link(
        "pages/1_Analyze.py",
        label="📷 Analyze Your Sky",
        use_container_width=True
    )

st.divider()

st.caption(
    "SkyReveal v1.0 • Making light pollution visible through accessible technology."
)
