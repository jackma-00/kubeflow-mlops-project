import kfp
from kfp.dsl import ContainerOp, pipeline, InputArgumentPath
from kfp import compiler

# Component's images
LOAD_DATASET_IMAGE = 'jackma00/load-dataset:latest'
NORMALIZE_DATASET_IMAGE = 'jackma00/normalize_dataset:latest'

# Building components from images
def load_dataset_component():
    return ContainerOp(
        name='Load Data',
        image=LOAD_DATASET_IMAGE,
        #command=[], # The entry point has already been provided with the Dockerfile
        arguments=[], # None
        file_outputs={'raw_dataset': 'app/raw_dataset.csv'})

def normalize_dataset_component(raw_dataset):
    return ContainerOp(
        name='Normalize Data',
        image=NORMALIZE_DATASET_IMAGE,
        #command=[], # The entry point has already been provided with the Dockerfile
        arguments=['--raw_dataset', raw_dataset],
        file_outputs={'normalized_dataset': 'app/normalized_dataset.csv'})


# Define the pipeline
@pipeline(
    name='data-pipeline',
    description='This simple data pipeline wants to test the custom created components')
def data_pipeline():
    load_dataset_task = load_dataset_component()

    normalize_dataset_task = normalize_dataset_component(
        raw_dataset=InputArgumentPath(load_dataset_task.file_outputs['raw_dataset'])).after(load_dataset_task)

# Compile the pipeline
compiler.Compiler().compile(
    pipeline_func=data_pipeline,
    package_path='data_pipeline.yaml')