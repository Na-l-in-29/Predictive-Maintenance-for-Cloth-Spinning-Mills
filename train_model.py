import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pickle
import os
from imblearn.over_sampling import SMOTE

# Load dataset
data = pd.read_csv('dataset/maintenance_data.csv')

# Preprocess data
X = data[['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]']]
y = data['Failure Type']  # Target variable

# Convert categorical labels to numerical
y = y.astype('category').cat.codes

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Handle class imbalance using SMOTE
smote = SMOTE(random_state=42)
X_train, y_train = smote.fit_resample(X_train, y_train)

# Model training with class weights
model = RandomForestClassifier(class_weight="balanced", random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred, zero_division=0))

# Create 'models' directory if not exists
os.makedirs('models', exist_ok=True)

# Save the model
with open('models/model.pkl', 'wb') as f:
    pickle.dump(model, f)
 