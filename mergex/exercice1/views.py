from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def index(request):
    return render (request, 'exercice1/index.html', {})
    """ return HttpResponse('<p>Lorem</p>') """

def pied_de_page(request):
    return render(request, 'exercice1/footer.html', {})