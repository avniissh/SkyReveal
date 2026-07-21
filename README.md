# SkyReveal
SkyReveal was created to raise awareness about light pollution by making night sky analysis accessible through computer vision.

**SkyReveal** is an educational web application that helps users understand the impact of light pollution on the night sky.

By analyzing a photograph of the night sky using computer vision, SkyReveal estimates sky quality and provides insights into how artificial lighting may affect star visibility.

---

## Features

- Upload a night sky photograph
- Detect visible stars using OpenCV
- Estimate background sky darkness
- Estimate cloud conditions
- Generate a Sky Quality Index
- Receive educational insights and recommendations
- Learn about light pollution through built in information pages

---

## Built With

- Python
- Streamlit
- OpenCV
- NumPy
- Pillow

---

## Project Structure

```text
SkyReveal/
│
├── app.py
├── pages/
│   ├── 1_Analyze.py
│   ├── 2_Learn.py
│   └── 3_About.py
│
├── modules/
│   ├── detector.py
│   ├── analyzer.py
│   ├── scorer.py
│   └── validator.py
│
├── requirements.txt
└── README.md
```

---

## General

Clone the repository:

```bash
git clone https://github.com/avniissh/SkyReveal.git
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## How It Works

1. Upload a photograph of the night sky.
2. SkyReveal detects bright star like objects using computer vision.
3. The image is analyzed for sky darkness, contrast, and cloud conditions.
4. A Sky Quality Index and educational report are generated.

---

## Disclaimer

SkyReveal is designed as an educational tool and does not replace professional sky quality measurements. Results may vary depending on camera settings, weather conditions, moonlight, and surrounding artificial lighting.

---

## Future Improvements

- Improved sky segmentation
- Better cloud detection
- Shareable result cards
- Bortle Scale estimation
- Location based recommendations
- Community sky submissions

---
