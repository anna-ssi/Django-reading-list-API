# Reading List

## Installation

Prerequisites:
```sh
Python 3.6, virtualenv, pip installed
virtualenv -p python3.6 venv
source venv/bin/activate
pip install -r requirements.txt
Copy .env.example to .env and fill in necessary fields
```

Db
```sh
python manage.py makemigrations books

python manage.py migrate
```

Run API:
```sh
python manage.py runserver
```
