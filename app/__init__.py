"""
Module: app/__init__.py

Purpose:
Contains the application factory function `create_app`, which initializes and 
configures the Flask application. Delegates logging setup to `logger.py`.

Details:
- Uses the application factory pattern for flexible configuration.
- Assigns a custom logger to `app.logger`, allowing flexibility to add other handlers.
"""

from flask import Flask  # Import the Flask class to create an app instance.
from .configs import Configs  # Import the selected configuration class.
from .logger import setup_logger  # Import the logger setup function.


def create_app():
    """
    Application factory function for creating and configuring the Flask app.

    Returns:
        app (Flask): The initialized and configured Flask application instance.
    """
    app = Flask(__name__)  # Create the Flask application instance.
    app.config.from_object(Configs)  # Load configuration settings into the app.

    # Set up and assign the custom logger
    app.logger = setup_logger()

    return app  # Return the configured app instance.
