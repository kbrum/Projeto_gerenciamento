from django.urls import path
from menu_principal.views import index

urlpatterns = [
    path('', index)
    
]