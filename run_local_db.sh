#!/bin/bash

source .env

DB_HOST=$LOCAL_DB_HOST
DB_NAME=$LOCAL_DB_NAME
DB_PASSWORD=$LOCAL_DB_PASSWORD
DB_PORT=$LOCAL_DB_PORT

docker rm -f $LOCAL_DB_NAME

docker run --name $LOCAL_DB_NAME \
    -e POSTGRES_PASSWORD=$LOCAL_DB_PASSWORD \
    -p $DB_PORT:5432 \
    -v postgres_data:/var/lib/postgresql/data \
    -d postgres:$LOCAL_DB_VERSION
