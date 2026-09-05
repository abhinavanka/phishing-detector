import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv("data/phishing.csv")

# Separate features (X) from the label (y)
X = df.drop(columns=["Index", "class"])   # everything except the row number and the answer
y = df["class"]                            # the answer: 1 = safe, -1 = phishing

# Split into training data and testing data (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Test how well it learned
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Model accuracy: {accuracy:.2%}")