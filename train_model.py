import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# 1. Load the data you collected
if not os.path.exists('pill_data.csv'):
    print("Error: pill_data.csv not found! Run your collector script first.")
    exit()

# Replace your current df = pd.read_csv line with these two lines:
df = pd.read_csv('pill_data.csv', header=None, names=['h', 's', 'v', 'label']) 

# 2. Separate features (H, S, V) from the answer (Label)
X = df[['h', 's', 'v']]  # Input data
y = df['label']          # What we want to predict

# 3. Create and Train the model
# We use RandomForest because it's very good at "grouping" colors
model = RandomForestClassifier(n_estimators=100)
print("Training the brain...")
model.fit(X, y)

# 4. Save the model to a file
joblib.dump(model, 'pill_model.pkl')
print("Success! 'pill_model.pkl' has been created.")