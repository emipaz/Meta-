from django.shortcuts import render
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import Libro

@csrf_exempt
def libros(request):
    if request.method == 'GET':
        libros = Libro.objects.all().values()
        return JsonResponse({'libros': list(libros)}, status=200)
    
    elif request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        precio = request.POST.get('precio')
        libro = Libro(titulo=titulo, autor=autor, precio=precio)
        try:
            libro.save()
        except IntegrityError:
            return JsonResponse({'error': 'true', 'message': 'Falta un campo'}, status=400)
        return JsonResponse(model_to_dict(libro), status=201)
