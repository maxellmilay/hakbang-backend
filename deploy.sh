#!/bin/bash

# Set the path to your service account key file
export GOOGLE_APPLICATION_CREDENTIALS="key.json"

# Authenticate with Google Cloud using the service account
gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS

# Set your project ID
gcloud config set project lakbai-439310

# Set default region for Cloud Run (optional)
gcloud config set run/region us-central1

gcloud auth configure-docker us-central1-docker.pkg.dev --quiet

# Variables
PROJECT_ID="lakbai-439310"
LOCATION="us-central1"
REPOSITORY="lakbai"
IMAGE="lakbai-backend"
TAG="latest"

IMAGE_NAME=$LOCATION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY/$IMAGE
IMAGE_URI=$IMAGE_NAME:$TAG

# Build Docker image
docker build --platform linux/amd64 -t $IMAGE_URI .

# Push the Docker image to Google Artifact Registry
docker push $IMAGE_URI

# Deploy to Cloud Run
gcloud run deploy lakbai-backend \
  --image=$IMAGE_URI \
  --platform=managed \
  --region=us-central1 \
  --allow-unauthenticated \
  --memory=2G \
  --cpu=2
  