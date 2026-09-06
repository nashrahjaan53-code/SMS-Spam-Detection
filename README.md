# SMS Spam Detection

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458?logo=pandas&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3%2B-F7931E?logo=scikitlearn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7%2B-11557C?logo=plotly&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-0.12%2B-4B8BBE?logo=python&logoColor=white)

> **Mini Project given by [DevTown](https://www.devtown.in/)**  
> Day 5 – NLP in Python Bootcamp

---

## Problem Statement

Build a Machine Learning model that can automatically classify an SMS message as **Ham** (normal) or **Spam** (unwanted).

---

## Dataset

- Source: [SMS Spam Collection Dataset (UCI)](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
- Total Messages: 5572
- Columns: Category (ham/spam), Message

---

## Project Structure
SMS-Spam-Detection/
├── data/
│   └── spam.csv
├── images/
│   ├── spam_vs_ham.png
│   └── confusion_matrix.png
├── spam_detection.py
├── requirements.txt
└── README.md


---

## Installation

```bash
pip install -r requirements.txt

How to Run
python spam_detection.py

Tasks Completed
Load and explore the dataset
Visualize Spam vs Ham distribution
Convert labels (Ham → 0, Spam → 1)
Split data into 80% training and 20% testing
Convert text into numbers using CountVectorizer (removed stopwords)
Train Logistic Regression model
Make predictions on test data
Evaluate the model (Accuracy + Confusion Matrix)
Test custom SMS messages

Results
Accuracy: ≈ 97.85%

The model classified 1091 messages correctly out of 1115.

Spam vs Ham Distribution
Confusion Matrix

Model Details:
Component,Technology Used
Algorithm,Logistic Regression
Feature Extraction,CountVectorizer (Bag of Words)
Stopwords,English stopwords removed
Train-Test Split,80% - 20%

How to Test Your Own Message
When you run the script, it will ask:
Enter an SMS message:
Type any message and press Enter. The model will reply with either:

HAM MESSAGE
SPAM MESSAGE