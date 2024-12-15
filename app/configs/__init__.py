"""
Package: configs

Purpose:
This package contains configuration settings for the Flask app, 
organized into modules for different environments.

Modules:
- base_config: Contains common configuration settings shared across environments.
- dev_config: Contains settings specific to the development environment.
- prod_config: Contains settings specific to the production environment.

Usage:
The appropriate configuration is selected automatically based on the 
`ENV` environment variable, with "development" as the default.
"""

import os
from dotenv import load_dotenv

# Load the environment variables from a .env file located in the parent directory.
dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path=dotenv_path, override=True)

# Retrieve the current environment setting, defaulting to "development".
env = os.getenv("ENV", "development")

# Load the appropriate configuration class based on the environment.
if env == "development":
    from .dev_config import DevelopmentConfig as Configs
elif env == "production":
    from .prod_config import ProductionConfig as Configs
else:
    # Raise an error for unsupported environments.
    raise ValueError(f"Unknown environment: {env}")
