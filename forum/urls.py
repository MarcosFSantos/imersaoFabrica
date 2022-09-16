from django.urls import path
from forum.views import pagPrincipal

urlpatterns = [
    path('', pagPrincipal),
]