from django import forms

class ContactForm(forms.Form):
    sub=forms.CharField(max_length=25)
    content=forms.CharField(widget=forms.Textarea,min_length=5)
    name=forms.CharField(max_length=30)
    contact=forms.CharField(max_length=20)
    email=forms.EmailField(label='e-mail address:',)
