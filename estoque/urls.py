from django.urls import path
from estoque.views import index

urlpatterns = [
    path('estoque/', index)
    
]