"""
Django command to wait fr the Db to be available
"""

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """ wait for the database """
    def handle(self, *args, **options):
        pass
        