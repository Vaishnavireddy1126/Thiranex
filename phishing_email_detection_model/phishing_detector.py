import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import FeatureUnion
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.pipeline import Pipeline

# Dataset format:
# text,label
# "Verify your account now",phishing
# "Meeting at 3 PM",safe

class URLFeatureExtractor(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        features = []
        for text in X:
            url_count = len(re.findall(r'https?://|www\.', str(text)))
            suspicious_words = len(re.findall(
                r'verify|urgent|password|bank|click|login|account|free',
                str(text).lower()))
            features.append([url_count, suspicious_words])
        return features

dataset = pd.read_csv("emails.csv")

X = dataset["text"]
y = dataset["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = Pipeline([
    ("features", FeatureUnion([
        ("tfidf", TfidfVectorizer(stop_words="english")),
        ("url_features", URLFeatureExtractor())
    ])),
    ("classifier", LogisticRegression(max_iter=1000))
])

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report:")
print(classification_report(y_test, predictions))

while True:
    email = input("\nEnter email text (or 'quit'): ")
    if email.lower() == "quit":
        break

    result = model.predict([email])[0]
    print("Prediction:", result.upper())
