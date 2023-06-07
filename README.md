# Cloud Computing Path

## How to Setup Locally
ini ya sak

## Google Cloud Platform Flow
<p align="center">
    <img width="460" alt="Screenshot 2023-06-07 at 23 22 07" src="https://github.com/C23-DF02-DiskusAI-Dicoding-Indonesia/API-Serving/assets/132810595/afeab717-152e-4d08-9b8c-59a838b06a7c">
</p>

The deployment flow in Google Cloud Platform (GCP) starts with the source code of the application or service that needs to be deployed. The source code then goes through the build, test, and packaging process using the Cloud Build service. The result of this process is a container image that is ready to be used.

The container image is temporarily stored in Cloud Storage before being uploaded to the Container Registry. Cloud Storage serves as a temporary storage for the files needed in the deployment process. After that, the container image is uploaded to the Container Registry, which is a secure storage for container images.

*Vertex AI Workbench can be used to manage machine learning experiments, train models, and deploy pipelines, with the results also being stored in Cloud Storage.

Once the container image is available in the Container Registry, the deployment process takes place in the Cloud Run service. Cloud Run is a serverless service that allows easy deployment of containers. The container image is fetched from the Container Registry and executed in the Cloud Run environment. Cloud Run automatically handles scaling, traffic management, and running containers as per the requests.

Lastly, the API Gateway can be used to provide a centralized API management layer. The API Gateway handles authentication, authorization, monitoring, and traffic policy settings for the APIs. With the API Gateway, users can access the deployed application or service using predefined endpoints.

With this flow, the source code goes through the build, packaging, and deployment process to Cloud Run via Cloud Build, Cloud Storage, Vertex AI Workbench (if applicable), and the Container Registry. Then, the application can be accessed through the API Gateway to provide centralized and managed access to the deployed application or service.

## How to Deploy using Google Cloud Run (Command)

Clone Source Repository
```bash
  cd ~ git clone https://github.com/antsaka/company-based-capstone-dicoding-df2.git
  cd ~/C23-DF02-DiskusAI-Dicoding-Indonesia
  ./setup.sh
```
Start Web Server
```bash
  cd ~/C23-DF02-DiskusAI-Dicoding-Indonesia/diskusai-app 
  npm start
```
Create Docker container with Cloud Build
```bash
  gcloud services enable cloudbuild.googleapis.com
  
  #Start Build Process
  gcloud builds submit --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/container name .
  
  #Deploy container to Cloud Run
  gcloud run deploy --image=gcr.io/${GOOGLE_CLOUD_PROJECT}/container name --platform managed
  
  #Verify Deployment
  gcloud run services list
```
Create Revision (example : concurrency)
```bash
  gcloud run deploy --image=gcr.io/${GOOGLE_CLOUD_PROJECT}/container name --platform managed --concurrency (insert number of concurrency)
```
Make changes to the website
```bash
  cd ~/C23-DF02-DiskusAI-Dicoding-Indonesia/Machine Learning Exploration/Search Bar Suggestion/templates
mv index.html.new index.html
 cat ~/C23-DF02-DiskusAI-Dicoding-Indonesia/Machine Learning Exploration/Search Bar Suggestion/templates/index.html
```
Trigger a new Cloud Build with an updated image version
```bash
  cd ~/C23-DF02-DiskusAI-Dicoding-Indonesia/container name

  #Test application 
   npm start 

  gcloud builds submit --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/container name:2.0.0 .
```
Redeploy
```bash
  gcloud run deploy --image=gcr.io/${GOOGLE_CLOUD_PROJECT}/container name:2.0.0 --platform managed
  
  #Verify Deployment
  gcloud run services describe diskusai-app --platform managed
```
Clean up
```bash
  gcloud container images delete gcr.io/${GOOGLE_CLOUD_PROJECT}/container name --quiet
```
