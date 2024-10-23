#!/bin/bash

# Set default region for Cloud Run (optional)
gcloud config set run/region us-central1

# Variables
PROJECT_ID="lakbai-439310"
LOCATION="us-central1"
REPOSITORY="lakbai"
IMAGE="lakbai-backend"
TAG="latest"

IMAGE_NAME=$LOCATION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY/$IMAGE
IMAGE_URI=$IMAGE_NAME:$TAG

gcloud auth configure-docker us-central1-docker.pkg.dev

# Build Docker image
docker build -t $IMAGE_URI .

# Push the Docker image to Google Artifact Registry
docker push $IMAGE_URI

# Deploy to Cloud Run
gcloud run deploy lakbai-backend \
  --image=$IMAGE_URI \
  --platform=managed \
  --region=us-central1 \
  --allow-unauthenticated
