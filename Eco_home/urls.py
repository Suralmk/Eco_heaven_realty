from django.urls import path
from .views import *


urlpatterns = [
        path('', homes, name='homes'),
        path('home-detail/<slug:home_url>/<int:pk>/', home_detail, name='home-detail'),

        path ('homes/', searched_homes, name='searched-homes')
        
]