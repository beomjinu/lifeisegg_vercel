#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.conf import settings

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)

    create_super_user()


def create_super_user(): # for vercel
    if not settings.DEBUG:
        if not User.objects.filter(username=settings.ADMIN_NAME).exists():
            User.objects.create_superuser(username=settings.ADMIN_NAME, email=settings.ADMIN_EMAIL, password=settings.ADMIN_PASSWORD)

if __name__ == '__main__':
    main()
