from typing import Any
from test_django.models import AboutPage,ContactData
from django.core.management import BaseCommand
from test_django.forms import ContactForm

class Commands(BaseCommand):
    def handle(self,*args,**kwargs):
        ContactData.objects.create(name=ContactForm.name,email = ContactForm.email,message=ContactForm.message)
        self.stdout.write(self.style.SUCCESS("Completed inserting data in db."))    