from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('imagem.html/',views.imagem)
]