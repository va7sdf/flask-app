"""
Module: logger.py

Purpose:
Provides a custom logger for the Flask application, with log rotation and flexibility 
to add other handlers in the future. Replaces the default Flask logger configuration.

Details:
- Logs application messages to `flask-app.log` in the `app/logs` directory.
- Rotates logs after reaching 10MB, keeping the last 7 log files.
- Returns the logger instance, allowing easy addition of other handlers.
"""

import os
import logging
from logging.handlers import RotatingFileHandler


def setup_logger():
    """
    Creates and configures a custom logger for the Flask application.

    Returns:
        logger (Logger): The configured logger instance.
    """
    # Create a logger instance for the application
    logger = logging.getLogger("flask-app")
    logger.setLevel(logging.DEBUG)

    # Ensure the logger is not configured multiple times
    if logger.handlers:
        return logger

    # Create the logs directory if it doesn't exist
    log_directory = os.path.join(os.path.dirname(__file__), "logs")
    os.makedirs(log_directory, exist_ok=True)

    log_file = os.path.join(log_directory, "flask-app.log")

    # Configure the rotating file handler (10MB per file, 7 backups)
    file_handler = RotatingFileHandler(
        log_file, maxBytes=10 * 1024 * 1024, backupCount=7
    )
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )
    # Configure custom level for file handler
    file_handler.setLevel(logging.INFO)
    logger.addHandler(file_handler)

    # Optionally, add a console handler for development
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    )
    # Configure custom level for console handler
    console_handler.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)

    return logger
