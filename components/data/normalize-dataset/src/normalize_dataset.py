import argparse
import pandas as pd
from sklearn.preprocessing import StandardScaler

def normalize_dataset(raw_dataset):
    """The function loads the input dataset and normalizes it"""

    # Load raw dataset
    df = pd.read_csv(raw_dataset)
    labels = df.pop('Labels')

    # Initialize the scaler
    scaler = StandardScaler()

    df = pd.DataFrame(scaler.fit_transform(df))
    df['Labels'] = labels

    return df

def save_dataset(df):
    """Teh function saves the normalized dataset into the running container"""

    # Save dataset
    df.to_csv('normalized_dataset.csv')


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--raw_dataset')
    args = parser.parse_args()

    print('Normalizing data ...')
    
    # Normalize dataset 
    normalized_dataset = normalize_dataset(args.raw_dataset)

    # Save dataset
    save_dataset(normalized_dataset)