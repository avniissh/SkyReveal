import cv2 as cv
import numpy as np


def analyze_image(img):
    """
    Analyze the underlying sky background rather than allowing the brightest
    stars or Milky Way regions to dominate the brightness measurement.

    Returns:
        background_brightness
        contrast
    """

    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

    # Ignore the brightest 10% of pixels.
    # These may contain stars, the Milky Way, the Moon,
    # or nearby artificial lights.

    brightness_limit = np.percentile(gray, 90)

    background_pixels = gray[gray < brightness_limit]

    if background_pixels.size == 0:
        background_brightness = float(np.mean(gray))
    else:
        background_brightness = float(np.mean(background_pixels))

    contrast = float(np.std(gray))

    return background_brightness, contrast


def estimate_cloud_cover(avg_brightness, contrast):
    """
    Produce a rough cloud estimate using brightness and image texture.

    This remains an educational estimate rather than a reliable
    meteorological cloud measurement.
    """

    # Smooth clouds often create a bright image with little texture.
    if avg_brightness > 90 and contrast < 20:
        return "High"

    elif avg_brightness > 55 and contrast < 30:
        return "Moderate"

    else:
        return "Low"