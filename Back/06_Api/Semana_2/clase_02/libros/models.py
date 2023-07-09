from django.db import models


class Categoria(models.Model):
    titulo = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo

class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="libros")

