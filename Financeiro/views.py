from django.shortcuts import render

def index(request):
    return render(request,'financeiro/index.html')

def contas_a_pagar(request):
    return render(request, 'financeiro/contas_a_pagar.html')

def contas_a_receber(request):
    return render(request, 'financeiro/contas_a_receber.html')
