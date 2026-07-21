def validate_image(avg_brightness, contrast, star_count):

    warnings = []

    if avg_brightness > 120:
        warnings.append(
            "This image appears very bright. Make sure it was taken at night."
        )

    if star_count < 5:
        warnings.append(
            "Very few stars were detected. Cloud cover, blur, or nearby lights may reduce accuracy."
        )

    if contrast < 15:
        warnings.append(
            "The image has low contrast. Results may be less reliable."
        )

    return warnings