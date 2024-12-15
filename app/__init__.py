"""
Module: app/__init__.py

Purpose:
This module contains the application factory function `create_app`, 
which initializes and configures the Flask application.

Details:
- Uses the application factory pattern to allow flexible configuration 
  based on the environment or testing needs.
- Loads the configuration settings from the `configs` package.
"""

from flask import Flask  # Import the Flask class to create an app instance.
from .configs import Configs  # Import the selected configuration class.


def create_app():
    """
    Application factory function for creating and configuring the Flask app.

    Returns:
        app (Flask): The initialized and configured Flask application instance.
    """
    app = Flask(__name__)  # Create the Flask application instance.
    app.config.from_object(Configs)  # Load configuration settings into the app.

    return app  # Return the configured app instance.
