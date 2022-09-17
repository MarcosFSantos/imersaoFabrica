from django.urls import path
from forum.views import pagPrincipal, pagTopico, pagCriarTopico, pagAtualizarTopico, pagDeletarTopico, pagCriarComentario, pagAtualizarComentario

urlpatterns = [
    path('', pagPrincipal, name='principal'),
    path('topico/<int:pk>', pagTopico, name='topico'),
    path('criarTopico/', pagCriarTopico, name='criarTopico'),
    path('atualizarTopico/<int:pk>/', pagAtualizarTopico, name='atualizarTopico'),
    path('deletarTopico/<int:pk>/', pagDeletarTopico, name='deletarTopico'),
    path('criarComentario/', pagCriarComentario, name='criarComentario'),
    path('atualizarComentario/<int:pk>', pagAtualizarComentario, name='atualizarComentario'),
]