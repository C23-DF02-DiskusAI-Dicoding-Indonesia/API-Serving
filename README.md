# Cloud Computing Path

## How to Setup Locally

To set up the provided Flask application locally, including using a virtual environment and activating it, follow these steps:

* Create a new directory for your project and navigate into it:
```bash
mkdir flask-app
cd flask-app
```
* Create a virtual environment using venv:
```bash
python3 -m venv env
```

* Create a virtual environment using venv:
On Windows:
```bash
env\Scripts\activate
```
On macOS/Linux:
```bash
source env/bin/activate
```

* Save the provided code in a file named app.py within the flask-app directory.
* Install the required dependencies by running the following command:
```bash
pip install flask flask_cors tensorflow numpy
```
Start the Flask development server:
```bash
flask run
```
or
```bash
python app.py
```

You should see output similar to the following:
```csharp
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
* The Flask application is now running locally.



## Google Cloud Platform Flow
<p align="center">
    <img width="460" alt="Screenshot 2023-06-07 at 23 22 07" src="https://github.com/C23-DF02-DiskusAI-Dicoding-Indonesia/API-Serving/assets/132810595/afeab717-152e-4d08-9b8c-59a838b06a7c">
</p>

The deployment flow in Google Cloud Platform (GCP) starts with the source code of the application or service that needs to be deployed. The source code then goes through the build, test, and packaging process using the Cloud Build service. The result of this process is a container image that is ready to be used.

The container image is temporarily stored in Cloud Storage before being uploaded to the Container Registry. Cloud Storage serves as a temporary storage for the files needed in the deployment process. After that, the container image is uploaded to the Container Registry, which is a secure storage for container images.

*Vertex AI Workbench can be used to manage machine learning experiments, train models, and deploy pipelines, with the results also being stored in Cloud Storage*

Once the container image is available in the Container Registry, the deployment process takes place in the Cloud Run service. Cloud Run is a serverless service that allows easy deployment of containers. The container image is fetched from the Container Registry and executed in the Cloud Run environment. Cloud Run automatically handles scaling, traffic management, and running containers as per the requests.

Lastly, the API Gateway can be used to provide a centralized API management layer. The API Gateway handles authentication, authorization, monitoring, and traffic policy settings for the APIs. With the API Gateway, users can access the deployed application or service using predefined endpoints.

With this flow, the source code goes through the build, packaging, and deployment process to Cloud Run via Cloud Build, Cloud Storage, Vertex AI Workbench (if applicable), and the Container Registry. Then, the application can be accessed through the API Gateway to provide centralized and managed access to the deployed application or service.

## Create IAM (roles)
- Choose IAM & Admin in on navigation menu 
- Click the "Add" button
- Choose Create a new role
- Provide a name and description for the role
- Select the desired permissions for the role
- Click Create to create the role.

## Cloud SQL Setup (MySQL)
- Database version : MySQL 8.0.26
- Region : asia-southeast2 (Jakarta)
- Machine type : 1 vCPU, 0.614 GB
- Storage type : SSD (100 GB)
- Availability : Multiple zones

## Create Cloud Storage
- Choose Cloud Storage on navigation menu 
- Click Create Bucket 
- Name your bucket as you wish 
- Location : Region and choose asia-southeast2 (Jakarta) 
- Create the Bucket
- Upload the image to the bucket

## Cloud Run Service Setup
- Region : asia-southeast2 (Jakarta)
- Authentication : Allow unauthenticated invocations
- Container port : chatbot-serving-integrated (2000), diskusai-app-fe-integrated (4000), searchbar-serving (5000)
- Capacity : 512 MiB - 2 GiB
- Maximum concurrent requests per instance : 80

## Deploy using Google Cloud Run (Manual)
- Click `Create Service`
- Import `Container Image URL`
- Select Region to `asia-southeast2 (Jakarta)`
- Choose `CPU is only allocated during request processing`
- `Allow unauthenticated invocations` for authentication 
- Click `Container, Networking, Security` and change the `Container Port` based on the container image
- Adjust the `Capacity` according to the size of the container image
- Click `Create`

## Deploy using Google Cloud Run (Command)

Clone Source Repository
```bash
  cd ~ git clone https://github.com/antsaka/C23-DF02-DiskusAI-Dicoding-Indonesia
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
Create Revision 
```bash
  #example : concurrency
  gcloud run deploy --image=gcr.io/${GOOGLE_CLOUD_PROJECT}/container name --platform managed --concurrency (insert number of concurrency)
```
Make changes to the website
```bash
   #examples
  cd ~/C23-DF02-DiskusAI-Dicoding-Indonesia/API-Serving/chatbot-serving
mv results.json.new results.json
 cat ~/C23-DF02-DiskusAI-Dicoding-Indonesia/API-Serving/chatbot-serving/results.json
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

## The Result of Deployment
- chatbot-serving-integrated : https://chatbot-serving-integrated-shx4zogvqq-et.a.run.app
- diskusai-app-fe-integrated : https://diskusai-app-fe-integrated-shx4zogvqq-et.a.run.app
- searchbar-serving : https://searchbar-serving-shx4zogvqq-et.a.run.app
