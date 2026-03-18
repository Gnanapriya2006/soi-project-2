import os
import numpy as np
from PIL import Image
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Configuration
DATASET_DIR = "dataset"
REAL_DIR = os.path.join(DATASET_DIR, "real")
FAKE_DIR = os.path.join(DATASET_DIR, "fake")
MODEL_PATH = "model.pkl"
IMG_SIZE = (64, 64) # Resize images to this for simple feature extraction

def load_data():
    data = []
    labels = []
    
    # Load Real Images (Label: 1)
    if not os.path.exists(REAL_DIR):
        print("Dataset not found! Run generate_dataset.py first.")
        return [], []
        
    print("Loading Real images...")
    for filename in os.listdir(REAL_DIR):
        if filename.endswith(".png"):
            filepath = os.path.join(REAL_DIR, filename)
            try:
                img = Image.open(filepath).convert('RGB')
                img = img.resize(IMG_SIZE)
                img_array = np.array(img).flatten() # Flatten 64x64x3 -> 12288 features
                data.append(img_array)
                labels.append(1) # Authentic
            except Exception as e:
                print(f"Error loading {filename}: {e}")

    # Load Fake Images (Label: 0)
    print("Loading Fake images...")
    for filename in os.listdir(FAKE_DIR):
        if filename.endswith(".png"):
            filepath = os.path.join(FAKE_DIR, filename)
            try:
                img = Image.open(filepath).convert('RGB')
                img = img.resize(IMG_SIZE)
                img_array = np.array(img).flatten()
                data.append(img_array)
                labels.append(0) # Fake
            except Exception as e:
                print(f"Error loading {filename}: {e}")
                
    return np.array(data), np.array(labels)

def train():
    print("Preparing data...")
    X, y = load_data()
    
    if len(X) == 0:
        print("No data loaded.")
        return

    print(f"Data shape: {X.shape}")
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train
    print("Training Random Forest Classifier...")
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    
    # Evaluate
    preds = clf.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"Model Accuracy: {acc * 100:.2f}%")
    
    # Save
    joblib.dump(clf, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    train()
