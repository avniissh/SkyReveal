import streamlit as st
import cv2 as cv
import numpy as np
from PIL import Image

from modules.detector import detect_stars
from modules.analyzer import analyze_image, estimate_cloud_cover
from modules.scorer import calculate_pollution_score
from modules.validator import validate_image

st.set_page_config(
    page_title="Analyze Your Sky",
    page_icon="📷",
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

# Helper functions

def get_quality_display(sky_quality_index):
    if sky_quality_index >= 80:
        return "Excellent", "⭐⭐⭐⭐⭐"
    elif sky_quality_index >= 60:
        return "Good", "⭐⭐⭐⭐"
    elif sky_quality_index >= 40:
        return "Fair", "⭐⭐⭐"
    elif sky_quality_index >= 20:
        return "Poor", "⭐⭐"
    else:
        return "Very Poor", "⭐"


def get_star_visibility_label(star_visibility_score):
    if star_visibility_score >= 80:
        return "Excellent"
    elif star_visibility_score >= 60:
        return "Good"
    elif star_visibility_score >= 40:
        return "Fair"
    elif star_visibility_score >= 20:
        return "Limited"
    else:
        return "Very Limited"


def get_darkness_label(darkness_score):
    if darkness_score >= 80:
        return "Very Dark"
    elif darkness_score >= 60:
        return "Dark"
    elif darkness_score >= 40:
        return "Moderately Bright"
    elif darkness_score >= 20:
        return "Bright"
    else:
        return "Very Bright"


def get_contrast_label(contrast_score):
    if contrast_score >= 80:
        return "Excellent"
    elif contrast_score >= 60:
        return "Good"
    elif contrast_score >= 40:
        return "Fair"
    elif contrast_score >= 20:
        return "Low"
    else:
        return "Very Low"

# Page introduction

st.title("📷 Analyze Your Sky")

st.write(
    """
    Upload a photograph taken outdoors at night. SkyReveal will create an
    educational estimate of night-sky quality using visible image features.
    """
)

uploaded_file = st.file_uploader(
    "Upload a night-sky image",
    type=["jpg", "jpeg", "png"],
    help=(
        "For the best results, upload an outdoor night photograph "
        "with as little foreground and nearby lighting as possible."
    )
)


if uploaded_file is not None:

    try:
        image = Image.open(uploaded_file).convert("RGB")
        img = np.array(image)

    except Exception:
        st.error(
            "SkyReveal could not read this image. "
            "Please upload a valid JPG, JPEG, or PNG file."
        )
        st.stop()

    st.image(
        img,
        caption="📷 Your Night Sky",
        use_container_width=True
    )

    with st.spinner("Analyzing your night sky..."):

        # Image analysis
        stars, _ = detect_stars(img)
        avg_brightness, contrast = analyze_image(img)

        cloud_cover = estimate_cloud_cover(
            avg_brightness,
            contrast
        )

        star_count = len(stars)

        results = calculate_pollution_score(
            avg_brightness,
            contrast,
            star_count,
            cloud_cover
        )

        sky_quality_index = results["sky_quality_index"]
        pollution_level = results["pollution_level"]

        quality_label, quality_stars = get_quality_display(
            sky_quality_index
        )

        star_visibility_label = get_star_visibility_label(
            results["star_visibility_score"]
        )

        darkness_label = get_darkness_label(
            results["darkness_score"]
        )

        contrast_label = get_contrast_label(
            results["contrast_score"]
        )

        warnings = validate_image(
            avg_brightness,
            contrast,
            star_count
        )

        # Draw detected stars
        output = img.copy()

        for x, y, w, h in stars:
            center_x = x + w // 2
            center_y = y + h // 2

            cv.circle(
                output,
                (center_x, center_y),
                4,
                (255, 255, 0),
                1
            )

    st.image(
        output,
        caption="Bright Stars Detected by SkyReveal",
        use_container_width=True
    )

    # Image-quality notices
    if warnings:
        st.info(
            "SkyReveal found some image conditions that may affect accuracy."
        )

        for warning in warnings:
            st.write(f"• {warning}")

    # Main report
    st.header("🌌 Your Night Sky")

    quality_col, pollution_col = st.columns(2)

    with quality_col:
        st.metric(
            "Sky Quality Index",
            f"{sky_quality_index}/100"
        )

    with pollution_col:
        st.metric(
            "Light Pollution Level",
            pollution_level
        )

    st.progress(sky_quality_index / 100)

    st.markdown(
        f"## {quality_label} Sky Quality {quality_stars}"
    )

    # Summary
    st.subheader("Summary")

    if sky_quality_index >= 80:
        st.success(
            """
            This photograph suggests excellent observing conditions,
            with a dark background and strong star visibility.
            """
        )
    elif sky_quality_index >= 60:
        st.success(
            """
            This photograph suggests good night-sky conditions.
            Some faint stars may still be hidden by skyglow, haze,
            clouds, moonlight, or camera settings.
            """
        )
    elif sky_quality_index >= 40:
        st.warning(
            """
            This photograph suggests fair night-sky conditions.
            Artificial lighting or atmospheric conditions may be
            hiding many fainter stars.
            """
        )
    elif sky_quality_index >= 20:
        st.error(
            """
            This photograph suggests poor night-sky visibility.
            Strong skyglow or difficult weather conditions may be
            hiding most faint astronomical objects.
            """
        )
    else:
        st.error(
            """
            This photograph suggests very poor night-sky visibility.
            The result may be affected by heavy light pollution,
            clouds, haze, or unsuitable image conditions.
            """
        )

    # Analysis breakdown
    st.subheader("Analysis Breakdown")

    st.markdown("### ⭐ Star Visibility")
    st.write(
        f"**{star_count} bright stars detected — "
        f"{star_visibility_label} visibility**"
    )
    st.progress(results["star_visibility_score"] / 100)

    st.markdown("### 🌑 Sky Darkness")
    st.write(f"**{darkness_label} background sky**")
    st.progress(results["darkness_score"] / 100)
    st.caption(
        f"Background brightness measurement: {avg_brightness:.2f}"
    )

    st.markdown("### 📈 Image Contrast")
    st.write(
        f"**{contrast_label} star-to-background separation**"
    )
    st.progress(results["contrast_score"] / 100)
    st.caption(f"Contrast measurement: {contrast:.2f}")

    st.markdown("### ☁️ Cloud Conditions")
    st.write(f"**Estimated cloud cover: {cloud_cover}**")
    st.progress(results["cloud_condition_score"] / 100)

    # What may be hidden
    st.subheader("✨ What You May Be Missing")

    if sky_quality_index < 40:
        st.write(
            """
            Under darker and clearer skies, you may be able to see:

            - hundreds of additional stars
            - complete constellation patterns
            - bright star clusters
            - the Milky Way under suitable conditions
            """
        )
    elif sky_quality_index < 70:
        st.write(
            """
            A darker location or clearer night may reveal:

            - additional faint stars
            - clearer constellations
            - richer star fields
            - improved chances of seeing the Milky Way
            """
        )
    else:
        st.write(
            """
            Your photograph already suggests strong observing conditions.

            A clear, moonless night and a longer exposure may reveal
            additional faint stars and deep-sky detail.
            """
        )

    # Recommendations
    st.subheader("📷 Recommendations")

    recommendations = []

    if cloud_cover == "High":
        recommendations.append(
            "Try again on a clearer night because clouds can hide stars."
        )
    elif cloud_cover == "Moderate":
        recommendations.append(
            "A clearer night may reveal significantly more faint stars."
        )

    if avg_brightness > 70:
        recommendations.append(
            "Move farther away from streetlights and illuminated buildings."
        )

    if contrast < 15:
        recommendations.append(
            "Keep your phone steady or use a tripod for a clearer image."
        )

    if star_count < 10:
        recommendations.append(
            "Try taking the photograph on a moonless night with fewer nearby lights."
        )

    if not recommendations:
        recommendations.append(
            "Conditions look promising. Try night mode or a longer exposure "
            "to capture fainter stars."
        )

    for recommendation in recommendations:
        st.write(f"• {recommendation}")

    st.info(
        """
        SkyReveal provides an image-based educational estimate rather than
        a professional scientific measurement. Camera exposure, editing,
        moonlight, clouds, haze, foreground objects, and nearby lights may
        influence the result.
        """
    )