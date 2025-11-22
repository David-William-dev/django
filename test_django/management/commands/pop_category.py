from typing import Any
from test_django.models import Category
from django.core.management import BaseCommand

class Command(BaseCommand):
    help = "insert category data    "
    def handle(self,*args,**kwargs):
        categories = ['sports','technology','nature','fun','Science','Art','Food']
        for category in categories:
            Category.objects.create(name = category)

        self.stdout.write(self.style.SUCCESS("Completed inserting data in db."))    