import cv2 as cv
import numpy as np


def detect_stars(img):
    """
    Detect small, bright, approximately circular objects that may be stars.

    Returns:
        stars: A list of bounding boxes in the format (x, y, width, height)
        avg_brightness: Kept temporarily for use in app.py
    """

    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

    avg_brightness = float(np.mean(gray))

    # Reduce sensor noise while keeping bright star-like objects visible.
    blurred = cv.GaussianBlur(gray, (5, 5), 0)

    params = cv.SimpleBlobDetector_Params()

    # Search across a suitable brightness range.
    params.minThreshold = 10
    params.maxThreshold = 255
    params.thresholdStep = 10

    # Stars should usually be small compared with clouds or foreground objects.
    params.filterByArea = True
    params.minArea = 2
    params.maxArea = 80

    # Stars are generally compact rather than long or irregular.
    params.filterByCircularity = True
    params.minCircularity = 0.4

    # Detect bright blobs.
    params.filterByColor = True
    params.blobColor = 255

    # These filters may reject valid stars in real phone photographs,
    # so they are disabled for now.
    params.filterByConvexity = False
    params.filterByInertia = False

    detector = cv.SimpleBlobDetector_create(params)

    keypoints = detector.detect(blurred)

    stars = []

    for keypoint in keypoints:
        center_x = int(keypoint.pt[0])
        center_y = int(keypoint.pt[1])

        # Use the detected blob size rather than forcing every box to be 6x6.
        size = max(4, int(keypoint.size))

        x = center_x - size // 2
        y = center_y - size // 2

        stars.append((x, y, size, size))

    return stars, avg_brightness