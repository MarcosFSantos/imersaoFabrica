from django.db import models

# Classe que representa os tópicos onde os usuários vão debater assuntos diversos no Forum de conversas.
class Topico(models.Model):
    Titulo = models.CharField(max_length=80, null=False, blank=False) #Título obrigatório do tópico.
    Autor = models.CharField(max_length=20, null=False, blank=False) #Nome obrigatório do autor do tópico.
    
    