from datetime import datetime
from django.db import models

# Classe que representa os tópicos onde os usuários vão debater assuntos diversos no Forum de conversas.
class Topico(models.Model):
    titulo = models.CharField(max_length=80, null=False, blank=False) # Título obrigatório do tópico.
    autor = models.CharField(max_length=20, null=False, blank=False) # Nome obrigatório do autor do tópico.
    conteudo = models.CharField(max_length=500, null=False, blank=True) # Mensagem do tópico explicando a discursão de um certo assunto.
    horaPostagem = models.DateTimeField(default = datetime.now, blank = True) # Hora atual identificada automaticamente pelo sistema.

    def __str__(self):
        return self.titulo
