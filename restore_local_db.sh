#!/bin/bash

source .env

DB_USER=$LOCAL_DB_USER
DB_HOST=$LOCAL_DB_HOST
DB_NAME=$LOCAL_DB_NAME
DB_PASSWORD=$LOCAL_DB_PASSWORD
DB_PORT=$LOCAL_DB_PORT

# Check if the SQL file path is provided as an argument
if [ -z "$1" ]; then
  echo "(ERROR) Please follow the following format: $0 path/to/your_file.sql"
  exit 1
fi

SQL_FILE_PATH="$1"

./run_local_db.sh

sleep 5

PGPASSWORD="$DB_PASSWORD" psql -U $DB_USER -h $DB_HOST -p $DB_PORT -tc "SELECT 1 FROM pg_database WHERE datname = '$DB_NAME'" | grep -q 1 || PGPASSWORD="$DB_PASSWORD" psql -U $DB_USER -h $DB_HOST -p $DB_PORT -c "CREATE DATABASE $DB_NAME;"
PGPASSWORD="$DB_PASSWORD" psql -U $DB_USER -h $DB_HOST -p $DB_PORT -d $DB_NAME < $SQL_FILE_PATH
