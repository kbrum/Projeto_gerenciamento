from django.shortcuts import render

def index(request):
    return render(request, 'pedidos/index.html')

def doces(request):
    return render(request, 'pedidos/doces.html')

def salgados(request):
    return render(request, 'pedidos/salgados.html')