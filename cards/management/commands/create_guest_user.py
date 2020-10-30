import pathlib
import sys

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
import yaml


class Command(BaseCommand):
    help = 'Creates a guest user'

    def handle(self, *args, **options):

        if User.objects.count() == 1:
            print('Ya existe el usuario `guest`')
            sys.exit()

        guest = User(
            email='guest@mitopedia.com',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )
        guest.set_unusable_password()
        guest.save()
        print('Done!!!')
