"""
Module: dev_config.py

Purpose:
Defines the development-specific configuration class that inherits from 
the base configuration. This class can include settings specific to 
the development environment.

Details:
- Inherits all common settings from BaseConfig.
- Add development-only settings or overrides as needed.
"""

from .base_config import BaseConfig


class DevelopmentConfig(BaseConfig):
    """
    Configuration class for the development environment.
    Inherits common settings from BaseConfig and can add development-specific settings.
    """

    pass  # Add development-specific configurations here, if needed.
