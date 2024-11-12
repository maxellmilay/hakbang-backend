#!/bin/bash

source .env

DB_USER=$REMOTE_DB_USER
DB_HOST=$REMOTE_DB_HOST
DB_NAME=$REMOTE_DB_NAME
DB_PASSWORD=$REMOTE_DB_PASSWORD

# Check if the SQL file path is provided as an argument
if [ -z "$1" ]; then
  echo "(ERROR) Please follow the following format: $0 path/to/your_file.sql"
  exit 1
fi

SQL_FILE_PATH="$1"

PGPASSWORD="$DB_PASSWORD" psql -U $DB_USER -h $DB_HOST -tc "SELECT 1 FROM pg_database WHERE datname = '$DB_NAME'" | grep -q 1 || PGPASSWORD="$DB_PASSWORD" psql -U $DB_USER -h $DB_HOST -c "CREATE DATABASE $DB_NAME;"
PGPASSWORD="$DB_PASSWORD" psql -U $DB_USER -h $DB_HOST -d $DB_NAME < $SQL_FILE_PATH
