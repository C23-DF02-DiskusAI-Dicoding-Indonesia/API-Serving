# Cloud Computing Path

## How to Setup Locally
ini ya sak

## Google Cloud Platform Flow
<img width="460" alt="Screenshot 2023-06-07 at 23 22 07" src="https://github.com/C23-DF02-DiskusAI-Dicoding-Indonesia/API-Serving/assets/132810595/afeab717-152e-4d08-9b8c-59a838b06a7c">


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
