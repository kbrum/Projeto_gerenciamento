from django.urls import path
from financeiro.views import index, contas_a_pagar, contas_a_receber

urlpatterns = [
    path('financeiro/', index),
    path('contas_pagar/', contas_a_pagar),
    path('contas_receber/', contas_a_receber),
    
]   