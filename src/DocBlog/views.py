# from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def index(request):
    # return HttpResponse("<h1>Bonjour, bienvenue sur mon site </h1>")
    date = datetime.today()
    # return render(request, "index.html", context={"prenom": "Ramoni"})
    return render(request, "DocBlog/index.html", context={"date":date}) 