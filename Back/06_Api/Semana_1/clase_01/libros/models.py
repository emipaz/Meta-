from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=5, decimal_places=2)

    

    def __str__(self):
        return self.titulo
