from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'TP1/about.html')

def contact(request):
    return render(request, 'TP1/contact.html')

def index(request):
    return render(request, 'TP1/index.html')
    
def project(request):
    return render(request, 'TP1/project.html')

def staff(request):
    return render(request, 'TP1/staff.html')
