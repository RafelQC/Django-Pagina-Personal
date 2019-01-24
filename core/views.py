from django.shortcuts import render, HttpResponse   

# Create your views here. vistas de la APP
"""def home(request):
    html_response = "<h1>Mi web personal</h1>"
    for i in range(10):
        html_response += "<h2>Portada</h2>"
    return HttpResponse(html_response)"""

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def portfolio(request):
    return render(request, "core/portfolio.html")

def contact(request):
    return render(request, "core/contact.html")