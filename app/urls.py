from django.urls import path
from .import views

urlpatterns = [

    path('', views.index, name='accueil'),
    path('accueil', views.index, name='accueil'),
    path('contact', views.contact, name='contact')
]