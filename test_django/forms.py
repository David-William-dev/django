# from django import forms

# class ContactForm(forms.Form):
#     name = forms.CharField(label="Name",max_length=100,required=True)
#     email = forms.EmailField(label="Email",required=True)
#     message = forms.CharField(label="Message",required=True)
# forms.py
from django import forms
from .models import ContactData

class ContactForm(forms.ModelForm):
    name = forms.CharField(label="Name", max_length=100, required=True)
    email = forms.EmailField(label="Email", required=True)
    message = forms.CharField(label="Message", required=True, widget=forms.Textarea)
    class Meta:
        model = ContactData
        fields = ['name', 'email', 'message']
