from django.core.management.base import BaseCommand
from Eco_app.models import User
from decouple import config
class Command(BaseCommand):
    help = 'Automatically creates a superuser'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(email=config("DJANGO_SUPERUSER_EMAIL")).exists():
            User.objects.create_superuser(first_name=config("DJANGO_SUPERUSER_FIRST_NAME"),last_name=config("DJANGO_SUPERUSER_LAST_NAME"), email=config("DJANGO_SUPERUSER_EMAIL"), password=config("DJANGO_SUPERUSER_PASSWORD"))
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists'))