from django.urls import path
from .views import *


app_name = 'home'
urlpatterns = [
    path('', landing_page, name='landing-page'),
]