# Vistas genéricas y ViewSets en DRF

## Introducción

DRF viene con muchas vistas genéricas y ViewSet para acelerar el desarrollo de API. Cuando usa estas clases, no necesita comenzar desde cero y usarlas reducirá el código en su proyecto de API. En esta lectura, aprenderá sobre los diferentes tipos de vistas genéricas y ViewSet , así como sus propósitos y beneficios.

## Conjuntos de vista

Los ViewSets son vistas simples basadas en clases, pero vienen con beneficios. Hay algunas clases ViewSets disponibles en DRF que puede usar para montar rápidamente un proyecto API CRUD en funcionamiento. También puede proporcionar clases de permiso y clases de aceleración para permitir llamadas API autenticadas y limitación de velocidad.

Para usar estas clases, debe importar el módulo de conjuntos de vistas desde rest_framework :  

```python
from rest_framework import viewsets
```

## Conjunto de vistas

Hay algunas clases de ViewSet , pero la base es ViewSet y amplía APIView . Cuando sus vistas basadas en clases extienden un ViewSet , obtiene vistas de API navegables listas para usar. Excepto por eso, cada ViewSet viene con una convención de nomenclatura de métodos para facilitar el enrutamiento de una línea que ahorra mucho tiempo.

Cuando se usa un ViewSet para manejar una colección de recursos, puede escribir su lógica comercial en los métodos list() y create() dentro de esta clase.


| Metodo de Clase | Método HTTP admitido |Objetivo |
|:---------------:|:--------------------:|:-------:|
|list()|GET|Mostrar colección de recursos|
|create()|POST|Crea un nuevo recurso|

Puede usar los siguientes métodos para escribir la lógica comercial cuando un ViewSet trata con un solo recurso.

| Metodo de Clase | Método HTTP admitido |Objetivo |
|:---------------:|:--------------------:|:-------:|
|retrieve()|GET|Mostrar un recurso singular|
|update()|PUT|Reemplace completamente un solo recurso con nuevos datos|
|partial_update()|PATCH| Actualizar parcialmente un solo recurso|
|destroy()|DELETE|Eliminar un solo recurso|

Cuando extienda un ViewSet , tendrá que escribir manualmente el código para realizar las operaciones de la base de datos. Pero hay dos clases ViewSet más que pueden hacer eso automáticamente por usted. Así es como se extiende una clase ViewSet .

```python
class MenuItemViewSet (viewsets.ViewSet)
```

## ModeloVistaConjunto

Si la vista basada en clases extiende un ModelViewSet , puede manejar automáticamente las operaciones CRUD por usted. Todo lo que debe hacer es darle a esta clase un conjunto de consultas y un serializador, y todo lo demás se hará automáticamente. Ya no necesita escribir código para todas esas operaciones de base de datos. Más adelante en este curso, verá un ejemplo práctico del uso de ModelViewSet para escribir un proyecto de API CRUD funcional con solo unas pocas líneas de código. Aquí hay un ejemplo de cómo extender este ViewSet .

```python
class MenuItemView (viewsets.ModelViewSet)
```

## ReadOnlyModelViewSet

Como sugiere el nombre, cuando sus vistas basadas en clases extienden un ReadOnlyModelViewSet , solo puede mostrar un único recurso y colección de recursos. Tales vistas no permiten ninguna operación de escritura, por lo que no maneja los métodos POST , PUT , PATCH o DELETE . Aquí hay un ejemplo de cómo extender un ReadOnlyModelViewSet .

```python
class ReadOnlyMenuItemView (viewsets.ReadOnlyModelViewSe
```

## Vistas genéricas

Las vistas genéricas son otra forma de escribir rápidamente vistas basadas en clases para andamiar proyectos API CRUD completamente funcionales. Hay varias vistas genéricas que ofrecen una funcionalidad particular, como mostrar recursos o crear un nuevo recurso, etc. Todo lo que debe hacer es ampliar estas vistas genéricas para que sus puntos finales de API funcionen.

Para usar estas clases de vista genéricas, debe importar el módulo generics desde rest_framework .

```python
from rest_framework import generics
```

Todas las clases de vistas genéricas requieren un conjunto de consultas y un serializador para funcionar correctamente.

Aquí hay una lista de vistas genéricas en DRF y sus propósitos.

| Clase de Vista | Método HTTP admitido |Objetivo |
|:---------------:|:--------------------:|:-------:|
|CreateAPIView|POST|Crea un nuevo recurso|
|ListAPIView|GET|Mostrar colección de recursos|
|RetrieveAPIView|GET|Mostrar un solo recurso|
|DestroyAPIView|DELETE|Elimina un simple recurso|
|UpdateAPIView|PUT and PATCH|Remplaza o Actualiza parcialmente un recurso|
|ListCreateAPIView|GET, POST|Muestra la colección de recursos y crea un nuevo recurso.|
|RetrieveUpdateAPIView|GET, PUT, PATCH|Mostrar un solo recurso y reemplazarlo o actualizarlo parcialmente|
|RetrieveDestroyAPIView|GET, DELETE|Mostrar un solo recurso y eliminarlo|
|RetrieveUpdateDestroyAPIView|GET, PUT, PATCH, DELETE|Mostrar, reemplazar o actualizar y eliminar un solo recurso|

## Código de ejemplo

Si desea que los extremos de la API puedan mostrar la recopilación de recursos y crear un nuevo recurso, debe extender tanto ListAPIView como CreateAPIView , o simplemente ListCreateAPIView . Las dos líneas de código siguientes hacen el mismo trabajo.

```python
class MenuItemView (generics.ListAPIView, generics.CreateAPIView)
```

y

```python
class MenuItemView (generics.ListCreateAPIView)
```

Al igual que ModelViewSet , debe otorgar a estas clases de vista genéricas un conjunto de consultas y un serializador y no necesita escribir código manualmente para realizar estas operaciones de base de datos.

## Autenticación y autenticación selectiva

Si desea que todas las llamadas a la API se autentiquen en una vista basada en clases que amplíe las vistas genéricas, puede agregar el atributo público allow_classes en la clase.

```python
Permission_classes = [IsAuthenticated]
```

Si desea habilitar de forma selectiva la autenticación para algunas llamadas, como POST , PUT , PATCH y DELETE , debe anular el método get_permission en su vista basada en clases de esta manera.

```python
def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
            
        return [permission() for permission in permission_classes]
```


## Devolver artículos solo para el usuario autenticado

A veces, en una vista basada en clases que amplía una vista genérica, es posible que desee devolver los recursos creados solo por los usuarios autenticados. En ese caso, debe anular el método get_queryset . El siguiente código en una vista basada en clases devuelve solo los pedidos creados por el usuario autenticado.

```python
class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Order.objects.all().filter(user=self.request.user)
```

## Anular el comportamiento predeterminado

Aunque las vistas genéricas automatizan todo, aún tiene un alcance completo para cambiar el comportamiento predeterminado anulando cualquiera de los métodos predeterminados. Aquí hay un ejemplo que devuelve una respuesta estática simple en lugar de los recursos.

```python
class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer  
    def get(self, request, *args, **kwargs):
        return Response(‘new response’)
```

Los otros métodos que puede anular son post() , put() , patch() y delete() .

Conclusión
---
En esta lectura, exploró las clases de ViewSet y las clases de vista genéricas que pueden ayudarlo a construir un proyecto de API CRUD completamente funcional en muy poco tiempo.