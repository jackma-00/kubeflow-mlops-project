import argparse
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

N_NEIGHBORS = 6

def train_knn(normalized_dataset):
    """The function trains a knn model."""

    # Load normalized dataset
    df = pd.read_csv(normalized_dataset)

    y = df.pop('Labels')
    X = df

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    clf = KNeighborsClassifier(n_neighbors=N_NEIGHBORS)
    clf.fit(X_train, y_train)
    
    return clf

def save_model(model):
    """The function serializes a model."""
    
    with open('knn.pkl', 'wb') as f:
        pickle.dump(model, f)

if __name__ == '__main__':

    # Parsing arguments 
    parser = argparse.ArgumentParser()
    parser.add_argument('--normalized_dataset')
    args = parser.parse_args()

    print("Training knn model ...")

    # Train model
    knn = train_knn(args.normalized_dataset)

    # Save model
    save_model(knn)
