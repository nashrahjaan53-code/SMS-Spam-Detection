# 📱 SMS Spam Detection

<div align="center">

### Machine Learning & NLP Classification Project

A machine learning system that automatically classifies SMS messages as **Ham** or **Spam** using Natural Language Processing and Logistic Regression.

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit Learn](https://img.shields.io/badge/Scikit--learn-1.3%2B-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7%2B-11557C?style=for-the-badge&logo=matplotlib&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-0.12%2B-4B8BBE?style=for-the-badge&logo=python&logoColor=white)

</div>

---

## 📌 Overview

Unwanted SMS messages are a common problem, ranging from promotional messages to fraudulent and malicious content.

This project builds an **NLP-based binary classification model** capable of analyzing the text of an SMS and predicting whether it is:

- 🟢 **Ham** — Normal / legitimate message
- 🔴 **Spam** — Unwanted or suspicious message

The project demonstrates a complete machine learning workflow, from **data preprocessing and exploratory analysis to text vectorization, model training, evaluation, and real-time prediction of custom messages.**

> 🎓 **Mini Project — DevTown NLP in Python Bootcamp**
>
> **Day 5: NLP in Python**

---

## 🎯 Problem Statement

Build a Machine Learning model that can automatically classify an SMS message as **Ham** or **Spam** based on its textual content.

The model should:

1. Load and preprocess the SMS dataset
2. Analyze the distribution of spam and legitimate messages
3. Convert text into numerical features
4. Train a classification model
5. Evaluate prediction performance
6. Allow users to test their own SMS messages

---

## 📊 Dataset

The project uses the **SMS Spam Collection Dataset**.

**Source:** [SMS Spam Collection Dataset — Kaggle](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)

| Property | Details |
|---|---|
| Total Messages | **5,572** |
| Classes | **Ham / Spam** |
| Input | SMS message text |
| Task | Binary classification |
| Feature Type | Natural language text |

---

## 🧠 Machine Learning Pipeline

```text
Raw SMS Dataset
       │
       ▼
Data Cleaning & Exploration
       │
       ▼
Label Encoding
(Ham → 0, Spam → 1)
       │
       ▼
Train / Test Split
(80% / 20%)
       │
       ▼
Text Preprocessing
       │
       ▼
CountVectorizer
(Bag-of-Words)
       │
       ▼
Logistic Regression
       │
       ▼
Predictions
       │
       ▼
Model Evaluation
       │
       ▼
Custom SMS Classification