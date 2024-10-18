from django.urls import path
from pedidos.views import index, doces, salgados 

urlpatterns = [
    path('pedidos/', index),
    path('pedidos/doces/', doces),
    path('pedidos/salgados/', salgados)

]