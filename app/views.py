from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from . models import *

def index(request):
    voiture=Voiture.objects.all().order_by('-id') [:6]
    marque= Marque.objects.all().order_by('marque')
    modele= Modele.objects.all().order_by('modele')
    etat= Etat.objects.all()
    data = {
        'voiture':voiture,
        'marque':marque,
        'modele':modele,
        'etat':etat,
    }
    return render(request, 'index.html', data)

def contact(request):
    return render(request, 'contact.html')

def list(request):
    voiture=Voiture.objects.all().order_by('-id')
    marque= Marque.objects.all().order_by('marque')
    data = {
        'voiture':voiture,
        'marque':marque,
    }
    return render(request, 'lists.html', data)