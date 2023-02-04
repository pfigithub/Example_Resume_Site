from Home_App.views import *
from django.urls import path

app_name = 'web'

urlpatterns = [
    path('', index, name = 'index'),
    path('about', about, name = 'about'),
    path('contact', contact, name = 'contact'),
    path('newsletter', newsletter_view, name = 'newsletter'),
]
