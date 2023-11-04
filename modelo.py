# calendario/modelo.py

from django.db import modelo

class Evento(modelo.Model):
    titulo = modelo.Charfield(max_lenght=100)
    fecha = modelo.DateField()
    hora_inicio = modelo.TimeField()
    hora_fin = modelo.TimeField

