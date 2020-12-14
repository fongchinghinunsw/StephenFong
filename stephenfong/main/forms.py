from django import forms

class ContactForm(forms.Form):
  name = forms.CharField(max_length=50)
  sender = forms.EmailField()
  subject = forms.CharField(max_length=100)
  message = forms.CharField(widget=forms.Textarea(attrs={'class': 'contact-textbox'}), max_length=2000)