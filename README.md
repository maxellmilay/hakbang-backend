<p>
  <img src="./documentation/banner.png"/>
</p>

## Database Model

Check out the design of our database [here](https://app.eraser.io/workspace/lkmTaoGm0ySUxUNpQ5Y2)

## Backend Setup

Follow the following steps to setup the backend part of Lakbai locally in Linux OS. You can still follow the steps on Windows, but you will have do identify the counterpart implementation.

### 1 - Clone this repository and navigate to root directory

```
git clone https://github.com/maxellmilay/lakbai.git
```

### 2 - Install Python and virtual environment (if not yet installed)

The Python version needs to be at least 3.10

```
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

### 3 - Create a virtual environment

```
python3 -m venv venv
```

### 4 - Activate virtual environemnt

```
source myenv/bin/activate
```

To deactivate, run `deactivate`

### 5 - Install dependencies

```
pip install -r requirements.txt
```

### 6 - Environment variables

Create a `.env` file in the root of the project directory, and then fill out the following ENV variables:

1. `OPEN_WEATHER_API_KEY=yourapikey`
2. `LOCAL_DB_HOST=localhost`
3. `LOCAL_DB_USER=postgres`
4. `LOCAL_DB_PASSWORD=postgres`
5. `LOCAL_DB_NAME=lakbai`
6. `LOCAL_DB_PORT=5440`
7. `LOCAL_DB_VERSION=13`

Replace `yourapikey` with you actual api key from OpenWeatherMaps, and copy the rest as is

**OPTIONAL**: If you want to use a remote database, you can also put your remote db secrets in the `.env` file, and prefix them with `REMOTE` (ex. `REMOTE_DB_NAME`)

### 7 - Setup script permissions

To proceed in the local setup, you need to enable permissions to run some shell scripts

Authorize the script to setup permissions
```
chmod +x ./setup_permissions.sh
```

Run script
```
./setup_permissions.sh
```

## Database Setup

You have two database choices here, and you can check them out in `main/settings.py`

1. SQLite3
2. PostgreSQL

Our team personally recommends setting up the PostgreSQL DB, but it requires Docker

### SQLite3

All you need to do is uncomment the SQLite3 config in `main/settings.py` (Uncomment the other database configs), and run migrations

```
python3 manage.py migrate
```

### PostgresSQL

You have the option to either start fresh with an empty database or import our existing data, but before everything, make sure that your Docker Enginer is running.

```
sudo systemctl start docker
```

Verify if Docker is running:

```
docker --version
```

After making sure that Docker is running, you run the script to start the Postgres 13 Database container

```
./run_local_db.sh
```

You can run `docker ps` to check if the container is up and running

#### Fresh DB Setup

For a clean database setup without any annotation, you can just run the following shell script:

```
./setup_db.sh
```

#### Load Existing Data

To load the database with our own data, you can run the script:

```
./restore_local_db.sh path/to/file.sql
```

Replace the `path/to/file.sql` with the actual file. You can select one of our backups from the `/db_backups` directory

Sample implementation
```
./restore_local_db.sh db_backups/2024-10-27_10-51-38.sql
```

## You are now good to go, happy hacking!
