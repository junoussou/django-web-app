from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1><br/><a href="../bonjour/">lien vers bonjour</a>')

def bonjour(request):
    return HttpResponse("""
    <h1>Bonjour les Zéros</h1>
    <p>J'apprend Django : les bases</p>
    <ul>
        <li>liste à puce 1</li>
        <li>liste à puce 2</li>
    </ul><br/><a href="../hello/">lien vers hello</a>
    """)

