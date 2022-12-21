import kfp
from kfp.v2.dsl import ContainerOp, Dataset, Input, pipeline, Output
from kfp import compiler

# Component's images
LOAD_DATASET_IMAGE = 'jackma00/load-dataset:latest'
NORMALIZE_DATASET_IMAGE = 'jackma00/normalize_dataset:latest'

# Building components from images
def load_dataset_component(raw_dataset: Output[Dataset]):
    return ContainerOp(
        name='Load Data',
        image=LOAD_DATASET_IMAGE,
        command=[], # The entry point has already been provided with the Dockerfile
        args=[], # None
        file_outputs={raw_dataset.path: 'app/raw_dataset.csv'})

def normalize_dataset_component(raw_dataset: Input[Dataset], 
                                normalized_dataset: Output[Dataset]):
    return ContainerOp(
        name='Normalize Data',
        image=NORMALIZE_DATASET_IMAGE,
        command=[], # The entry point has already been provided with the Dockerfile
        args=['--raw_dataset', raw_dataset.path],
        file_outputs={normalized_dataset.path: 'app/normalized_dataset.csv'})


# Define the pipeline
@pipeline(
    name='data-pipeline',
    description='This simple data pipeline wants to the the custom created components')
def data_pipeline():
    load_dataset_task = load_dataset_component()

    normalize_dataset_task = normalize_dataset_component(
        raw_dataset=load_dataset_task.outputs['raw_dataset'])

# Compile the pipeline
cmplr = compiler.Compiler(mode=kfp.dsl.PipelineExecutionMode.V2_COMPATIBLE)
cmplr.compile(pipeline_func=data_pipeline, package_path='data_pipeline.yaml')