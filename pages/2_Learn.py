import streamlit as st

st.set_page_config(
    page_title="Learn About Light Pollution",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

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

st.title("📚 Learn About Light Pollution")

st.markdown(
    """
    Light pollution is the excessive, unnecessary, or poorly directed use of
    artificial light at night.

    It can brighten the night sky, reduce the visibility of stars, and affect
    wildlife, ecosystems, energy use, and astronomical research.
    """
)

st.header("Types of Light Pollution")

st.subheader("Skyglow")
st.write(
    """
    The bright haze visible above cities and populated areas. Skyglow makes
    faint stars and the Milky Way difficult or impossible to see.
    """
)

st.subheader("Glare")
st.write(
    """
    Excessive brightness that causes discomfort and can reduce visibility.
    """
)

st.subheader("Light Trespass")
st.write(
    """
    Light that reaches places where it is not needed, such as outdoor lighting
    shining into homes.
    """
)

st.subheader("Clutter")
st.write(
    """
    Excessive groups of bright lights that create visual confusion and waste energy.
    """
)

st.header("Why It Matters")

st.write(
    """
    Light pollution can:

    - hide stars and the Milky Way
    - disturb nocturnal wildlife
    - disrupt natural migration and feeding patterns
    - waste electricity
    - interfere with astronomical observations
    - disconnect communities from the natural night sky
    """
)

st.header("What Can You Do?")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Use Light Only When Needed")
    st.write(
        "Switch off unnecessary outdoor lighting and use timers or motion sensors."
    )

    st.subheader("Point Lights Downward")
    st.write(
        "Use shielded fixtures so light reaches the ground rather than the sky."
    )

with col2:
    st.subheader("Choose Warmer Lighting")
    st.write(
        "Warmer lighting generally creates less blue-rich skyglow."
    )

    st.subheader("Reduce Brightness")
    st.write(
        "Use the lowest brightness required for the task."
    )

st.info(
    """
    Even small changes in outdoor lighting can reduce glare, save energy,
    and protect the night sky.
    """
)