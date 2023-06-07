# Cloud Computing Path

## How to Setup Locally
ini ya sak

## How to Deploy using Google Cloud Run

Clone Source Repository
```bash
  cd ~ git clone https://github.com/antsaka/company-based-capstone-dicoding-df2.git
  cd ~/company-based-capstone-dicoding-df2
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
  
  Start Build Process
  gcloud builds submit --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/docker name .
  
  Deploy container to Cloud Run
  gcloud run deploy --image=gcr.io/${GOOGLE_CLOUD_PROJECT}/docker name --platform managed
  
  Verify Deployment
  gcloud run services list
```
Create Revision of Concurrency
```bash
  gcloud run deploy --image=gcr.io/${GOOGLE_CLOUD_PROJECT}/container name --platform managed --concurrency (insert number of concurrency)
```
Make changes to the website
```bash
  cd ~/company-based-capstone-dicoding-df2/Machine Learning Exploration/Search Bar Suggestion/templates
mv index.html.new index.html
 cat ~/company-based-capstone-dicoding-df2/Machine Learning Exploration/Search Bar Suggestion/templates/index.html
```
Trigger a new Cloud Build with an updated image version
```bash
  cd ~/company-based-capstone-dicoding-df2/container name

  #Test application 
   npm start 

  gcloud builds submit --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/container name:2.0.0 .
```
Redeploy
```bash
  gcloud run deploy --image=gcr.io/${GOOGLE_CLOUD_PROJECT}/containe name:2.0.0 --platform managed
  
  Verify Deployment
  gcloud run services describe monolith --platform managed
```
Clean up
```bash
  gcloud container images delete gcr.io/${GOOGLE_CLOUD_PROJECT}/container name --quiet
```
