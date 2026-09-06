<div align="center">

📩 SMS Spam Detection
NLP-Based Binary Text Classification with Machine Learning
A machine learning project that automatically classifies SMS messages as Ham (legitimate) or Spam using text preprocessing, Bag-of-Words feature extraction, and Logistic Regression.






Mini Project • DevTown NLP in Python Bootcamp • Day 5

</div>

📌 Overview
Unwanted SMS messages are a common form of digital spam. Automatically identifying these messages requires a model that can learn patterns in natural language and distinguish legitimate communication from promotional or malicious content.

This project builds an end-to-end SMS spam classification pipeline using classical Natural Language Processing and supervised Machine Learning.

The workflow covers:

Data Exploration → Text Preprocessing → Feature Extraction → Model Training → Prediction → Evaluation → Custom Testing

🎯 Problem Statement
Build a Machine Learning model that can classify an SMS message into one of two categories:

Label	Meaning
Ham	Legitimate / normal message
Spam	Unwanted / suspicious message
The final model can also be used interactively to classify a custom SMS message entered by the user.

📊 Dataset
Dataset: SMS Spam Collection

Source: UCI SMS Spam Collection Dataset

Property	Details
Total Messages	5,572
Classes	Ham / Spam
Input	SMS message text
Target	Message category
The dataset contains real-world SMS messages labeled as either legitimate messages or spam.

🧠 Machine Learning Pipeline
SMS Dataset
     │
     ▼
Data Exploration
     │
     ▼
Label Encoding
Ham → 0
Spam → 1
     │
     ▼
Train / Test Split
80% / 20%
     │
     ▼
Text Vectorization
CountVectorizer
     │
     ▼
Logistic Regression
     │
     ▼
Predictions
     │
     ├───────────────┐
     ▼               ▼
Accuracy        Confusion Matrix
     │
     ▼
Custom SMS Testing
🔧 Tasks Completed
Loaded and explored the SMS dataset

Analyzed the distribution of Ham and Spam messages

Converted categorical labels into numerical values

Split the dataset into 80% training / 20% testing

Converted text into numerical features using CountVectorizer

Removed English stopwords during feature extraction

Trained a Logistic Regression classifier

Generated predictions on unseen test data

Evaluated the model using accuracy and a confusion matrix

Added interactive custom-message prediction
Model Details
Component	Technology
Problem Type	Binary Text Classification
Algorithm	Logistic Regression
Feature Extraction	CountVectorizer
Representation	Bag of Words
Stopwords	English stopwords removed
Train/Test Split	80% / 20%
Evaluation	Accuracy + Confusion Matrix
 Results
Model Accuracy
≈ 97.85%

The model correctly classified approximately 1,091 out of 1,115 messages in the test set.

Accuracy is calculated on the held-out test set and represents the performance of this particular train/test split.

 Visualizations
Spam vs Ham Distribution
The project visualizes the class distribution to understand the balance between legitimate and spam messages.


Confusion Matrix
The confusion matrix provides a detailed view of correct and incorrect predictions for both classes.


 Test Your Own SMS
The project includes an interactive prediction step.

Run the program and enter:

Enter an SMS message:
For example:

Congratulations! You have won a free prize. Claim now!
The model will classify the message as:

SPAM MESSAGE
For a normal message such as:

Hey, are we still meeting at 6?
The model should return:

HAM MESSAGE
 Project Structure
SMS-Spam-Detection/
│
├── data/
│   └── spam.csv
│
├── images/
│   ├── spam_vs_ham.png
│   └── confusion_matrix.png
│
├── spam_detection.py
├── requirements.txt
└── README.md
Installation
Clone the repository and install the required dependencies:

pip install -r requirements.txt
Or install the core libraries manually:

pip install pandas scikit-learn matplotlib seaborn
How to Run
Execute the main Python script:

python spam_detection.py
The program will:

Load the dataset

Prepare the text data

Train the classification model

Evaluate its performance

Display the confusion matrix

Allow you to test custom SMS messages

 Concepts Demonstrated
Natural Language Processing
Text classification

Stopword removal

Bag-of-Words representation

Feature extraction

Machine Learning
Supervised learning

Binary classification

Logistic Regression

Train/test splitting

Model evaluation

Data Analysis
Dataset exploration

Class distribution analysis

Confusion matrix interpretation

Performance evaluation

 Key Takeaways
This project demonstrates how raw text can be transformed into numerical features and used to build a practical classification system.

The main learning outcomes include:

Understanding the complete NLP → ML workflow

Converting unstructured text into machine-readable features

Training a baseline text classifier

Evaluating classification performance beyond simple predictions

Building an interactive prediction workflow

Possible Improvements
The current implementation uses a classical Bag-of-Words + Logistic Regression approach. It can be extended with:

TF-IDF feature extraction

Naive Bayes comparison

Linear SVM comparison

Hyperparameter tuning

Precision, Recall and F1-score analysis

ROC-AUC evaluation

N-gram features

Text normalization and stemming/lemmatization

Cross-validation

Model persistence using joblib

A Streamlit web interface

Project Highlights
5,572 SMS messages

97.85% test accuracy

End-to-end NLP pipeline

Binary spam classification

Bag-of-Words feature engineering

Logistic Regression

Confusion matrix analysis

Interactive custom-message prediction

<div align="center">

From Raw SMS Text → Machine Learning → Spam Detection
Built as part of the DevTown NLP in Python Bootcamp

</div>