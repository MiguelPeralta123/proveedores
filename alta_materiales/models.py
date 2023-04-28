from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Material(models.Model):
    empresa = models.CharField(max_length=50)
    nombre_producto = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    familia = models.CharField(max_length=50)
    subfamilia = models.CharField(max_length=50)
    unidad_medida = models.CharField(max_length=50)
    justificacion = models.CharField(max_length=255)
    compras = models.BooleanField(default=False)
    finanzas = models.BooleanField(default=False)
    sistemas = models.BooleanField(default=False)
    aprobadas = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " - " + self.nombre_producto + " - " + self.usuario.username