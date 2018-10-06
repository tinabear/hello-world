## Microservice source files
- hello-world.py
- Dockerfile
- docker-compose.yml
- deployment.yml (ansible playbook)

## Build & Test before deploying
- Use git post-commit push notification to trigger Jenkins CI pipeline.
- Run docker build to generate docker image.
- Start a docker container and run some smoke tests against this container.
- The whole process is managed by Jenkins pipelines.

## Versioning
- Basically, we can directly use git commit SHA as the version during build and tag the image with the git hash tag. So during deployment, use specific git hash tag to pull the micro service image.
- Here, the ansible playbook deployment.yml use a variable `service_tag` to pull the image. Be default, the latest version is deployed.

## Deployment & Scaling
- Use Jenkins to hook up automatic deployment with specific version (image tag). Since we are using ansible to start docker service, the deployment is just to run playbook `deployment.yml` file on the docker host or a swarm cluster. Basically, docker swarm services can be scaled with a command. Health check is used to determine whether the scale command needs to be run against docker swarm.
- Or, if we are using Kubernetes, the autoscale can be configured with `HorizontalPodAutoscaler` based on CPU metrics
