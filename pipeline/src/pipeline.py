import kfp
from kfp.dsl import ContainerOp, pipeline, InputArgumentPath
from kfp import compiler

# Component's images
LOAD_DATASET_IMAGE = 'jackma00/load-dataset:latest'
NORMALIZE_DATASET_IMAGE = 'jackma00/normalize-dataset:latest' 
TRAIN_KNN_IMAGE = 'jackma00/train-knn:latest'

# Building components from images
def load_dataset_component():
    return ContainerOp(
        name='Load Data',
        image=LOAD_DATASET_IMAGE,
        command=['python', 'load_dataset.py'], 
        file_outputs={'raw_dataset': 'raw_dataset.csv'})

def normalize_dataset_component(raw_dataset):
    return ContainerOp(
        name='Normalize Data',
        image=NORMALIZE_DATASET_IMAGE,
        command=['python', 'normalize_dataset.py'],
        arguments=['--raw_dataset', raw_dataset],
        file_outputs={'normalized_dataset': 'normalized_dataset.csv'})

def train_knn_component(normalized_dataset):
    return ContainerOp(
        name='Train knn Model',
        image=TRAIN_KNN_IMAGE,
        command=['python', 'train_knn.py'],
        arguments=['--normalized_dataset', normalized_dataset],
        file_outputs={'knn_model': 'knn.pkl'})


# Define the pipeline
@pipeline(
    name='pipeline',
    description='This simple pipeline wants to test the custom created components, as well as the CI/CD operations')
def pipeline():
    load_dataset_task = load_dataset_component()

    normalize_dataset_task = normalize_dataset_component(
        raw_dataset=InputArgumentPath(load_dataset_task.outputs['raw_dataset'])).after(load_dataset_task)

    train_knn_task = train_knn_component(
        normalized_dataset=InputArgumentPath(normalize_dataset_task.outputs['normalized_dataset'])).after(normalize_dataset_task)
