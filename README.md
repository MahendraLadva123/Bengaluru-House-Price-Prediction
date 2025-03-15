# Bengaluru-House-Price-Prediction

A web application to predict house prices in Bengaluru using a machine learning model.

[![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Model Training](#model-training)
- [Screenshot](#screenshot)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This project is a **Bengaluru House Price Prediction** application built with Flask. It allows users to input features such as location, square footage, number of bathrooms, and BHK configuration to estimate the house price in Bengaluru.

---

## Features

- **Interactive Web Interface:** Built with HTML, Bootstrap, and Flask.
- **Machine Learning Integration:** Uses a pre-trained model to predict house prices.
- **Data Preprocessing:** Leverages a cleaned dataset to improve prediction accuracy.
- **Error Handling:** Provides user-friendly error messages in case of invalid input.

---

## Project Structure

Bengaluru-House-Price-Prediction/ ├── app.py # Flask application file ├── Bengaluru price prediction.ipynb # Notebook for model training and exploration ├── bengaluru_house_prices.csv # Raw dataset ├── cleaned_data.csv # Preprocessed dataset ├── model1.pkl # Serialized machine learning model ├── index.html # Frontend template for the web app ├── README.md # Project documentation └── Output.png # Screenshot of the application UI


---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Bengaluru-House-Price-Prediction.git
cd Bengaluru-House-Price-Prediction

```bash
pip install flask pandas scikit-learn numpy

```bash
pip install -r requirements.txt

```bash
python app.py

```bash
http://127.0.0.1:5000/
