import argparse
import pandas as pd

def load_dataset():
    """The function loads the dataset from the URL."""

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

def save_dataset(df):
    """The function saves the dataset into the running container."""

    # Save dataset
    df.to_csv('raw_dataset.csv')


if __name__ == '__main__':

    print('Loading data ...')
    
    # Load dataset 
    dataset = load_dataset()

    # Save the dataset to the given path 
    save_dataset(dataset)