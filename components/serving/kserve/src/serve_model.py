import argparse
from kubernetes import client 
from kserve import KServeClient
from kserve import constants
from kserve import utils
from kserve import V1beta1InferenceService
from kserve import V1beta1InferenceServiceSpec
from kserve import V1beta1PredictorSpec
from kserve import V1beta1SKLearnSpec

def serve(model):
    """The function serves the given model with KServe."""
    
    # Adapt model uri to a s3 compatible one 
    #model_uri = model.path.replace('/minio/', 's3://')
    print(model)
    print(type(model))

    # This will retrieve the current namespace of your Kubernetes context. The InferenceService will be deployed in this namespace.
    namespace = utils.get_default_target_namespace()

    # Define the inference service
    name='iris-knn-predictor'
    kserve_version='v1beta1'
    api_version = constants.KSERVE_GROUP + '/' + kserve_version

    isvc = V1beta1InferenceService(api_version=api_version,
                                   kind=constants.KSERVE_KIND,
                                   metadata=client.V1ObjectMeta(
                                        name=name, namespace=namespace, annotations={'sidecar.istio.io/inject':'false'}),
                                   spec=V1beta1InferenceServiceSpec(
                                   predictor=V1beta1PredictorSpec(
                                   sklearn=(V1beta1SKLearnSpec(
                                        storage_uri=model))))
    )

    # Create the inference service
    KServe = KServeClient()
    KServe.create(isvc)


if __name__ == '__main__':

    # Parsing arguments 
    parser = argparse.ArgumentParser()
    parser.add_argument('--model')
    args = parser.parse_args()

    print("Serving model using KServe ...")

    # Serve model
    serve(args.model)