import argparse
import pandas as pd

def load_dataset():
    """The function load the dataset from the URL."""

    # URL where to retrieve the dataset
    csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    
    # using the attribute information as the column names
    col_names = [
        'Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width', 'Labels'
    ]

    # Load dataset
    df = pd.read_csv(csv_url, names=col_names)

    # Return dataset
    return df

def save_dataset(df, output_dataset_path):
    """The function save the dataset to the given path."""

    # Save dataset
    with open(output_dataset_path, 'w') as f:
        df.to_csv(f)


if __name__ == '__main__':

    # Parsing arguments 
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_dataset') # This will be the output dataset path (with respect to the storage type supported)
    args = parser.parse_args()

    print('Loading data ...')
    
    # Load dataset 
    dataset = load_dataset()

    # Save the dataset to the given path 
    save_dataset(dataset, args.output_dataset)