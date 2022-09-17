from django.urls import path
from forum.views import pagPrincipal, pagTopico

urlpatterns = [
    path('', pagPrincipal, name='principal'),
    path('topico/<int:pk>', pagTopico, name='topico'),
]