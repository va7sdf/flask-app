"""
Module: app/__init__.py

Purpose:
Contains the application factory function `create_app`, which initializes and 
configures the Flask application. Delegates logging setup to `logger.py`.

Details:
- Uses the application factory pattern for flexible configuration.
- Assigns a custom logger to `app.logger`, allowing flexibility to add other handlers.
- Registers a blueprint for the logging demo.
"""

from flask import Flask
from .configs import Configs
from .logger import setup_logger


def create_app():
    """
    Application factory function for creating and configuring the Flask app.

    Returns:
        app (Flask): The initialized and configured Flask application instance.
    """
    # Step 1: Create the Flask application instance
    app = Flask(__name__)

    # Step 2: Load configuration settings into the app
    app.config.from_object(Configs)

    # Step 3: Set up and assign the custom logger
    app.logger = setup_logger()

    # Step 4: Register the logging demo blueprint
    from .routes import logging_demo_bp
    app.register_blueprint(logging_demo_bp)

    app.logger.info("===== STARTING FLASK APP DEMO =====")

    # Return the configured app instance
    return app
