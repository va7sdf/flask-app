"""
Module: app.py

Purpose:
This is the entry point for the Flask application. It imports the application 
factory function `create_app` from the `app` package and initializes the 
Flask application instance.

Details:
- The `create_app` function is called to create and configure the Flask app.
- The app instance is exposed at the global level for deployment tools (e.g., WSGI).
"""

from app import create_app  # Import the application factory function.

# Create and configure the Flask application instance.
# The `__name__` argument helps Flask locate resources relative to the file's location.
app = create_app()
