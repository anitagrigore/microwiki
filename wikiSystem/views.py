from django.shortcuts import render
from .models import Pages


def index(request):
    pages = Pages.objects.all()
    return render(request, 'index.html', {'pages' : pages})


def view_wiki(request, id):
    page = Pages.objects.get(id=id)
    return render(request, 'wiki.html', {'page': page})


