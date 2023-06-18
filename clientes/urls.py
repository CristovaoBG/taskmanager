from django.urls import path
import include
from . import views

urlpatterns = [
    path('', views.clientes, name="clientes")
]
