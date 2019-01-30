from django.shortcuts import render
#importam els projectes del model project a portfolio per a poder importar les bases de dades amb els projectes
from .models import Project

# Create your views here.

def portfolio(request):
    #ens retorna tots els projectes que tenim guardats a la base de dades cap a la variable projects
    projects = Project.objects.all()
    #quan ens fan un request de la pagina, també incluim un diccionari amb tot el contingut dels projectes
    return render(request, "portfolio/portfolio.html", {'projects':projects})