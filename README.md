# Lakb.ai Backend

-   [Database model](https://app.eraser.io/workspace/lkmTaoGm0ySUxUNpQ5Y2)

## Setup (Unix)

### Clone this repository and navigate to root directory

### Install python and virtual environment (if not yet installed)

```
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

### Create a virtual environment

```
python3 -m venv venv
```

### Activate virtual environemnt

```
source myenv/bin/activate
```

To deactivate, run `deactivate`

### Install dependencies

```
pip install -r requirements.txt
```

### Migrate

```
python manage.py migrate
```

### Run server

```
python manage.py runserver
```
