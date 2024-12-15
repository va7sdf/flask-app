"""
Module: app/routes/views.py

Purpose:
Defines routes for the logging demo. Provides a page with buttons to trigger
log messages for different logging levels. 

Details:
- Includes a route for rendering the main logging demo page.
- Includes a route for triggering log messages based on the selected level.
"""

from flask import Blueprint, render_template, redirect, url_for, flash, current_app

# Define a Blueprint for the logging demo
logging_demo_bp = Blueprint("logging_demo", __name__)

# Route for the logging demo page
@logging_demo_bp.route("/")
def logging_demo():
    """
    Render a page with buttons for each logging level.

    Returns:
        str: The rendered HTML of the main demo page.
    """
    return render_template("main.html")  # Render the main demo page (template: main.html)


# Route for logging actions
@logging_demo_bp.route("/log/<level>")
def log_message(level):
    """
    Trigger a log message based on the selected logging level.

    Args:
        level (str): The logging level (e.g., debug, info, warning, error, critical).

    Returns:
        Response: A redirection to the main demo page with a flash message.
    """
    # Access the Flask application's logger
    logger = current_app.logger

    # Map the logging levels to their corresponding logger methods
    log_levels = {
        "debug": logger.debug,
        "info": logger.info,
        "warning": logger.warning,
        "error": logger.error,
        "critical": logger.critical,
    }

    # Check if the level is valid and log the message
    if level in log_levels:
        log_levels[level](f"This is a {level.upper()} message.")  # Log the message
        flash(f"{level.upper()} log message triggered!", "success")  # Flash success message
    else:
        flash("Invalid log level!", "danger")  # Flash error message for invalid levels

    # Redirect back to the main logging demo page
    return redirect(url_for("logging_demo.logging_demo"))
