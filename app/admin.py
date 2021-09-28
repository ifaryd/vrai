from django.contrib import admin


from . models import Etat, Voiture, Marque, Modele

admin.site.register(Voiture)
admin.site.register(Marque)
admin.site.register(Modele)
admin.site.register(Etat)