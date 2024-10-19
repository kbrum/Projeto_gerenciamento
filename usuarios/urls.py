from django.urls import path
from usuarios.views import index

urlpatterns = [
    path('usuarios/', index)
    
    
]