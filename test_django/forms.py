# from django import forms

# class ContactForm(forms.Form):
#     name = forms.CharField(label="Name",max_length=100,required=True)
#     email = forms.EmailField(label="Email",required=True)
#     message = forms.CharField(label="Message",required=True)
# forms.py
from django import forms
from .models import ContactData,Post,Category

class ContactForm(forms.ModelForm):
    name = forms.CharField(label="Name", max_length=100, required=True)
    email = forms.EmailField(label="Email", required=True)
    message = forms.CharField(label="Message", required=True, widget=forms.Textarea)
    class Meta:
        model = ContactData
        fields = ['name', 'email', 'message']

class PostForm(forms.ModelForm):
    title = forms.CharField(label="Title", max_length=200, required=True)
    content = forms.CharField(label="Content", required=True, widget=forms.Textarea)
    url = forms.URLField(label="Image URL", required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label="Category", required=True, empty_label="Select Category")
    img = forms.URLField(label="Image URL", required=False)
    class Meta:
        model = Post
        fields = ['title', 'content', 'img', 'category']