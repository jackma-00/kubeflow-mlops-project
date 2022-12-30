# Kubeflow Mlops Project

## Components
Each component is made up of a python script that performs some operations such as loading data, train models and serve them.

Each component is containerized into a docker container and the resulting image is pushed to the Docker Hub registry.

## Pipeline 
The pipeline is made up of many custom container components, which represent individual steps in the pipeline. 

Each component is executed in its own Docker container pulled from the registry and integrated with its own set of inputs, commands and outputs.

Note how each component is highly decoupled from one another and from the pipeline itself. Thank to the micro-service nature of each component we can rely on their interfaces built with the ContainerOp class.

## CI/CD
From the components perspective CI/CD operations have already been implemented by github actions pushing the newly built container images to the Docker Hub at each push to the main branch on github. 
Each time a new pipeline is compiled, up to date images are retrieved from the registry.

From the pipeline perspective, in order to deploy the newly compiled pipeline to the Kubeflow platform automatically, github actions should dispose of a public address where to find the platform. 

To do so, we should expose our Kubeflow platform over a load balancer.
Refer to the AWS documentation: https://awslabs.github.io/kubeflow-manifests/docs/add-ons/load-balancer/guide/ 

## CT
From there, the next steps would be to have only one model that is periodically retrained with client.create_recurring_run(), which would make what we just built your training pipeline.
You should then create an inference pipeline that only loads the model and makes predictions, which would allow you to set up another type of recurring — or on-demand — runs, without having to retrain the model every time. Finally, you should also have a monitoring pipeline that triggers the training pipeline when it detects a drop in the model’s performance.
You can also add a performance criterion in your CD so that your GitHub action only succeeds when a newly added feature improves the performance of the model.

## Issues 

### KServe
Despite giving the model artifact to the serving infrastructure, KServe is unable to retrieve and load it to the inference end point. Apparently it is looking for S3 artifact storage paths only.

### Pipelines SDK versions 
problems of inconsistency between documentation and the actual implementation on the SDK. Particularly with the V2 version.