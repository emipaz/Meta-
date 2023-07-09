from django.shortcuts import render
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import generics
from .models import Libro, Categoria
from .serializers import LibroSerializer, CategoriaSerializer

@csrf_exempt
@api_view(['GET', 'POST'])
def libros(request):
    if request.method == 'GET':
        libros = Libro.objects.all().values()
        #return JsonResponse({'libros': list(libros)}, status=200)
        return Response({'libros': list(libros)}, status=200)
    
    elif request.method == 'POST':
        libro_serializado = LibroSerializer(data=request.data)
        libro_serializado.is_valid(raise_exception=True)
        libro_serializado.save()
        return Response(libro_serializado.data, status.HTTP_201_CREATED)
    

class LibroView(APIView):
    def get(self, request, pk):
        libro = Libro.objects.get(id=pk)
        libro_serializado = LibroSerializer(libro)
        return Response(libro_serializado.data, status.HTTP_200_OK)
    
    def put(self, request, pk):
        libro = Libro.objects.get(id=pk)
        titulo = request.data.get('titulo')
        autor = request.data.get('autor')
        precio = request.data.get('precio')
        libro.titulo = titulo
        libro.autor = autor
        libro.precio = precio
        libro.save()
        libro_serializado = LibroSerializer(libro)
        return Response(libro_serializado.data, status.HTTP_200_OK)
    

class LibroViewGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    #permission_classes = [IsAuthenticated]
    #def get_queryset(self):
    #    return Libro.objects.all().filter(user=self.request.user)
    

class LibrosViewset(viewsets.ViewSet):
    def list(self, request):
        return Response({"message":"All books"}, status.HTTP_200_OK)
    def create(self, request):
        return Response({"message":"Creating a book"}, status.HTTP_201_CREATED)
    def update(self, request, pk=None):
        return Response({"message":"Updating a book"}, status.HTTP_200_OK)
    def retrieve(self, request, pk=None):
        return Response({"message":"Displaying a book"}, status.HTTP_200_OK)
    def partial_update(self, request, pk=None):
        return Response({"message":"Partially updating a book"}, status.HTTP_200_OK)
    def destroy(self, request, pk=None):
        return Response({"message":"Deleting a book"}, status.HTTP_200_OK)
    

class LibrosModelViewset(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer


@api_view()
def categoria_detail(request, pk):
    categoria = Categoria.objects.get(id=pk)
    categoria_serializada =CategoriaSerializer(categoria)
    return Response(categoria_serializada.data)

