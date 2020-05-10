#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import django
import discord
import random
import subprocess
import threading
import sys

"""
from discordsearch.services import InitiateEngine

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bluesearch.settings')
django.setup()
from discordsearch.models import Messages
from discordsearch.services import MessageHandler
"""

def start():
    """
    This is called the very first time when server runs
    Separate async subprocess is created to execute all discord tasks
    """

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bluesearch.settings')
    django.setup()

    #from discordsearch.services import initiateEngine

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bluesearch.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    start()
    main()
