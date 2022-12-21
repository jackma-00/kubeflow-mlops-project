import argparse
import pandas as pd
from sklearn.preprocessing import StandardScaler

def normalize_dataset(input_dataset_path):
    """The function loads the input dataset and normalizes it"""

    with open(input_dataset_path) as f:
        df = pd.read_csv(f)
        labels = df.pop('Labels')

    scaler = StandardScaler()

    df = pd.DataFrame(scaler.fit_transform(df))
    df['Labels'] = labels

    return df

def save_dataset(df, normalized_dataset_path):
    """Teh function saves the normalized dataset to the given path."""

    with open(normalized_dataset_path, 'w') as f:
        df.to_csv(f)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dataset')
    parser.add_argument('--normalized_dataset')
    args = parser.parse_args()

    print('Normalizing data ...')
    
    # Normalize dataset 
    normalized_df = normalize_dataset(args.input_dataset)

    # Save dataset
    save_dataset(normalized_df, args.normalized_dataset)