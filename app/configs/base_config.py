"""
Module: base_config.py

Purpose:
Defines the base configuration class with settings common to all 
environments. This serves as a foundation for environment-specific 
configuration classes.

Details:
- Contains shared settings applicable across all environments.
- Meant to be extended by specialized configuration classes.
"""


class BaseConfig:
    """
    The base configuration class with settings common to all environments.
    This class can be extended by environment-specific configurations.
    """

    SECRET_KEY = (
        "your-secret-key"  # Replace this with a secure, randomly generated key.
    )
