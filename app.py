import streamlit as st


st.set_page_config(
    page_title="SkyReveal",
    page_icon="🌌",
    layout="centered"
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


st.markdown(
    """
    ## How much of the night sky are you missing?

    SkyReveal is an accessible light-pollution awareness platform that uses
    computer vision to analyze photographs of the night sky.

    Upload your own sky photograph to explore star visibility, sky darkness,
    image contrast, and estimated light pollution.
    """
)

st.page_link(
    "pages/1_Analyze.py",
    label="📷 Analyze Your Sky",
    use_container_width=True
)

st.markdown("---")

st.header("Why SkyReveal?")

st.write(
    """
    Artificial lighting can wash out the night sky, making faint stars,
    constellations, and the Milky Way harder to see.

    SkyReveal turns a photograph into an easy-to-understand educational report,
    helping users see how artificial skyglow may affect their surroundings.
    """
)

st.header("How It Works")

step1, step2, step3 = st.columns(3)

with step1:
    st.subheader("1. Upload")
    st.write(
        "Choose a photograph of the night sky from your phone or camera."
    )

with step2:
    st.subheader("2. Analyze")
    st.write(
        "SkyReveal measures visible stars, darkness, contrast, and cloud conditions."
    )

with step3:
    st.subheader("3. Discover")
    st.write(
        "Receive a clear report explaining your sky and what may be hidden."
    )

st.markdown("---")

st.header("Explore SkyReveal")

col1, col2 = st.columns(2)

with col1:
    st.page_link(
        "pages/2_Learn.py",
        label="📚 Learn About Light Pollution",
        use_container_width=True
    )

with col2:
    st.page_link(
        "pages/3_About.py",
        label="ℹ️ About the Project",
        use_container_width=True
    )

st.markdown("---")

st.caption(
    "SkyReveal • Making light pollution visible through accessible technology."
)