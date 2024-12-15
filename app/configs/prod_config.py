"""
Module: prod_config.py

Purpose:
Defines the production-specific configuration class that inherits from 
the base configuration. This class can include settings specific to 
the production environment.

Details:
- Inherits all common settings from BaseConfig.
- Add production-only settings or overrides as needed.
"""

from .base_config import BaseConfig


class ProductionConfig(BaseConfig):
    """
    Configuration class for the production environment.
    Inherits common settings from BaseConfig and can add production-specific settings.
    """

    pass  # Add production-specific configurations here, if needed.
