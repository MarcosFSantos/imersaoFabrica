from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from forum.models import Topico

# Formulário utilizado para criação de um tópico.
class TopicoForm(ModelForm):
    class Meta:
        model = Topico
        fields = ['titulo', 'autor', 'conteudo']