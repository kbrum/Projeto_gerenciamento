from django.urls import path
from financeiro.views import index,

urlpatterns = [
    path('', index),