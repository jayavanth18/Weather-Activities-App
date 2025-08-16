# 🌤️ Weather & Activities App

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**A lightweight Python CLI app that fetches live weather data and suggests activities based on conditions.**

🎥 **[Watch the Demo](https://youtu.be/h_1Ll4w68Gs)**

</div>  

---

## 🌟 Overview

The **Weather & Activities App** is a Python-based command-line tool that:

* Fetches current weather using the **Open-Meteo API**
* Approximates **local time** based on city longitude
* Suggests **indoor/outdoor activities** tailored to the weather

This project gave hands-on experience with:

* REST APIs & JSON parsing
* Modular Python function design
* CLI interaction & error handling
* Basic **time zone math** for global usability

It’s designed to be **lightweight, beginner-friendly, and educational**, while also being well-structured for testing and clarity.

---

## ✨ Features

* 🌍 **Real-time Weather** – Uses Open-Meteo’s Geocoding & Weather APIs
* 🌦️ **Simplified Weather Codes** – Maps raw codes to conditions like *Clear*, *Rain*, *Snow*
* 🏃 **Activity Suggestions** – Indoor/outdoor recommendations based on current conditions
* ⏰ **Local Time Approximation** – Calculates time with the formula: `longitude / 15`
* 🧪 **Testable Design** – Includes unit tests for key functions

---

## 📂 Project Structure

```plaintext
Weather-Activities-App/
├── project.py        # Main CLI application
├── test_project.py   # Unit tests (activities, time conversion, weather codes)
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Weather-Activities-App.git
cd Weather-Activities-App
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the app from the command line:

```bash
python project.py
```

### Example Flow

1. Enter a **city name** (e.g., `Paris`)
2. App fetches **current weather** from Open-Meteo
3. Approximates **local time** using longitude
4. Suggests **activities** based on weather conditions

---

## 🧪 Testing

Unit tests are included for core functionality. Run with:

```bash
pytest test_project.py
```

---

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

<div align="center">

**[A. Jayavanth](https://github.com/jayavanth18)**

[![GitHub](https://img.shields.io/badge/GitHub-jayavanth18-black?logo=github)](https://github.com/jayavanth18)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/jayavanth18/)

⭐ If this repo helped you, consider giving it a **star**!

</div>  

---
