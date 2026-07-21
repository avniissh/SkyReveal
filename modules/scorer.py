def calculate_pollution_score(
    avg_brightness,
    contrast,
    star_count,
    cloud_cover
):
    # Higher darkness score means a darker sky.
    darkness_score = max(
        0,
        min(100, 100 - (avg_brightness / 120) * 100)
    )

    # More detected stars means better visibility.
    star_visibility_score = max(
        0,
        min(100, (star_count / 50) * 100)
    )

    # Higher contrast generally means stars stand out more clearly.
    contrast_score = max(
        0,
        min(100, (contrast / 45) * 100)
    )

    cloud_scores = {
        "Low": 90,
        "Moderate": 60,
        "High": 30
    }

    cloud_condition_score = cloud_scores.get(
        cloud_cover,
        50
    )

    sky_quality_index = int(
        darkness_score * 0.35
        + star_visibility_score * 0.45
        + contrast_score * 0.15
        + cloud_condition_score * 0.10
    )

    pollution_score = 100 - sky_quality_index

    if sky_quality_index >= 80:
        quality = "Excellent ⭐⭐⭐⭐⭐"
        pollution_level = "Very Low"

    elif sky_quality_index >= 60:
        quality = "Good ⭐⭐⭐⭐"
        pollution_level = "Low"

    elif sky_quality_index >= 40:
        quality = "Moderate ⭐⭐⭐"
        pollution_level = "Moderate"

    else:
        quality = "Poor ⭐⭐"
        pollution_level = "High"

    return {
        "sky_quality_index": sky_quality_index,
        "pollution_score": pollution_score,
        "quality": quality,
        "pollution_level": pollution_level,
        "darkness_score": int(darkness_score),
        "star_visibility_score": int(star_visibility_score),
        "contrast_score": int(contrast_score),
        "cloud_condition_score": cloud_condition_score
    }