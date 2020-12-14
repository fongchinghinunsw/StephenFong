from django.urls import path
from . import views

urlpatterns = [
  # views.home is a function
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('project/', views.project, name='project'),
  path('article/', views.article, name='article'),
  path('contact/', views.contact, name='contact'),
]