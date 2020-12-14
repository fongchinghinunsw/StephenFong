from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm


def home(request):
  return render(request, 'main/home.html')

def about(request):
  return render(request, 'main/about.html', {'title': 'About'})

def article(request):
  return render(request, 'main/article.html', {'title': 'Article'})

def project(request):
  return render(request, 'main/project.html', {'title': 'Project'})

def contact(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data['name']
      sender = form.cleaned_data['sender']
      subject = form.cleaned_data['subject']
      message = form.cleaned_data['message']

      recipients = ['fongchinghinstephen@gmail.com']
      send_mail(subject, message, sender, recipients)
      return render(request, 'main/contact.html')

  form = ContactForm()
  return render(request, 'main/contact.html', {'form': form})
