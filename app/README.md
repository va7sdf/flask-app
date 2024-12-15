# Flask Logging Demo

This demonstrates logging from within a Flask app using multiple custom logging handlers.

## Obtain Code

Clone project from GitHub

```sh
git clone https://github.com/va7sdf/flask-app.git
```

## Configure project

Create a virtual environment

```sh
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install the dependencies

```sh
pip install -r requirements.txt
```

## Run the project

Using Flask development server at http://localhost:5000 (or your machine's local IP address)

```sh
flask run --host 0.0.0.0
```

Using Gunicorn WSGI server at http://localhost:8000 (or your machine's local IP address)

```sh
gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app
```