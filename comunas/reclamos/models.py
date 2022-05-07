from django.db import models

class Comuna(models.Model):
    numero = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    class Meta:
        ordering = ['numero']

    def __str__(self):
        return f"Comuna {self.numero}"

class Reclamo(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    comuna = models.ForeignKey(Comuna, models.CASCADE)
    imagen = models.ImageField(upload_to='images/')
