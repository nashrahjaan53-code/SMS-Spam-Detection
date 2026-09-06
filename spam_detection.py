import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import os

os.makedirs('images', exist_ok=True)

df = pd.read_csv('data/spam.csv', encoding='latin-1')

if 'v1' in df.columns and 'v2' in df.columns:
    df = df[['v1', 'v2']]
    df.columns = ['Category', 'Message']

df = df[['Category', 'Message']]

print("First 5 rows:")
print(df.head())
print("\nShape of dataset (rows, columns):", df.shape)
print("\nNumber of Ham and Spam messages:")
print(df['Category'].value_counts())

plt.figure(figsize=(6,4))
df['Category'].value_counts().plot(kind='bar', color=['green', 'red'])
plt.title('Number of Spam vs Ham Messages')
plt.xlabel('Message Type')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('images/spam_vs_ham.png')
plt.show()

print("\nHam messages are more common in the dataset.")

df['Category'] = df['Category'].map({'ham': 0, 'spam': 1})

X = df['Message']
y = df['Category']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("\nTraining set size:", len(X_train))
print("Testing set size:", len(X_test))

vectorizer = CountVectorizer(stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

predictions = model.predict(X_test_vec)

accuracy = accuracy_score(y_test, predictions)
print(f"\nAccuracy of the model: {accuracy * 100:.2f}%")

cm = confusion_matrix(y_test, predictions)
print("\nConfusion Matrix:")
print(cm)

plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Ham (0)', 'Spam (1)'],
            yticklabels=['Ham (0)', 'Spam (1)'])
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.tight_layout()
plt.savefig('images/confusion_matrix.png')
plt.show()

correct = cm[0,0] + cm[1,1]
print(f"\nThe model classified {correct} messages correctly out of {len(y_test)}.")

print("\n" + "="*50)
print("Test your own SMS message")
print("="*50)

user_message = input("Enter an SMS message: ")
user_vec = vectorizer.transform([user_message])
pred = model.predict(user_vec)[0]

if pred == 0:
    print("\nHAM MESSAGE")
else:
    print("\nSPAM MESSAGE")