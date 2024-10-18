from django.urls import path
from pedidos.views import index, doces, salgados 

urlpatterns = [
    path('pedidos/', index),
    path('doces/', doces),
    path('salgados/', salgados)

]