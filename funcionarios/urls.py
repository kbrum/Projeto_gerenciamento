from django.urls import path
from funcionarios.views import index

urlpatterns = [
    path('funcionarios/', index)
    
    
]