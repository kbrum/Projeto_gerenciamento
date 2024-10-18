from django.shortcuts import render

def index(request):
    return render(request, 'principal_menu/index.html')
