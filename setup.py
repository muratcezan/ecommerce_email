# email/setup.py

"""Setup module for the ecommerce_email package.

This module provides the configuration for packaging the ecommerce_email library,
which contains utilities for sending emails via Flask-Mail.
"""

import os
from setuptools import setup, find_packages


def read_long_description():
    """Reads the README.md file if it exists, otherwise returns an empty string."""
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""


setup(
    name="ecommerce_email",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "Flask>=2.3.0",
        "Flask-Mail>=0.10.0",
    ],
    python_requires=">=3.9",
    author="Murat CEZAN",
    author_email="muratcezan@gmail.com",
    description="Flask-Mail integration utilities for sending emails in ecommerce projects.",
    long_description=read_long_description(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/muratcezan/ecommerce_email",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Flask",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
)
