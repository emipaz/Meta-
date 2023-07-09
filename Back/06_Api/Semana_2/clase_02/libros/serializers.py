from rest_framework import serializers
from .models import Libro, Categoria


# class LibroSerializer(serializers.Serializer):
#     titulo = serializers.CharField(max_length=255)
#     autor = serializers.CharField(max_length=255)
#     precio = serializers.DecimalField(max_digits=5, decimal_places=2)


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'titulo']


class LibroSerializer(serializers.ModelSerializer):
    #categoria = serializers.StringRelatedField(read_only=True)
    categoria_id = serializers.IntegerField(write_only=True)
    categoria = serializers.HyperlinkedRelatedField(
        queryset = Categoria.objects.all(),
        view_name='categoria-detail'
    )
    class Meta:
        model = Libro
        fields = ['id', 'titulo', 'autor', 'precio', 'categoria', 'categoria_id']