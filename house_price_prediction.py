import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import randomforest
import pickle

# Load dataset
df = pd.read_csv("Housing.csv")

# Convert yes/no columns
binary = [
    'mainroad','guestroom','basement',
    'hotwaterheating','airconditioning','prefarea'
]

for col in binary:
    df[col] = df[col].map({'yes': 1, 'no': 0})

# Convert categorical column
df = pd.get_dummies(df, columns=['furnishingstatus'])

# NOW select features
X = df.drop('price', axis=1)
y = df['price']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained successfully!")