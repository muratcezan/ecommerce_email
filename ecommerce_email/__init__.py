"""Package entry point for the email utility.

Provides a simple wrapper around Flask-Mail for sending emails in Flask applications.
"""

from .ecommerce_email import mail, init_mail, send_email

__all__ = ["mail", "init_mail", "send_email"]
