# Otros tipos de serializadores en DRF

## Introducción

Ahora conoce los serializadores en DRF y aprendió a usar serializadores de modelos para serializar relaciones de modelos. Esta lectura tiene algunos consejos y trucos interesantes con respecto a la serialización, como cómo mostrar automáticamente un campo de modelo anidado usando la opción de profundidad del serializador. También aprenderá a mostrar campos de modelos relacionados como hipervínculos usando HyperlinkedRelatedField o usando un nuevo tipo de serializador llamado HyperlinkedModelSerializer.


## Campos anidados

Si visitara el punto final de los elementos del menú , observaría que la categoría se muestra como un campo anidado con su id, título y slug.


![Alt text](image-1.png)

Esto puede lograrse de dos formas.

### Método 1

La primera forma de hacer esto es crear un serializador de categorías en serializers.py e incluirlo en el serializador de elementos de menú como se muestra en el código a continuación.

```python
from rest_framework import serializers
from decimal import Decimal
from .models import MenuItem, Category 

class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','slug','title']
 
class MenuItemSerializer(serializers.ModelSerializer):
    stock =  serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
    category = CategorySerializer()
    class Meta:
        model = MenuItem
        fields = ['id','title','price','stock', 'price_after_tax','category']
    
    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)

```

### Método 2

Hay otra manera de hacer esto. En lugar de declarar el campo de categoría como CategorySerializer , puede especificar que depth=1 esté en la clase Meta en MenuItemSerializer . De esta forma, todas las relaciones en este serializador mostrarán todos los campos relacionados con ese modelo. Puede cambiar el código de MenuItemSerializer como se muestra a continuación.

```python

class MenuItemSerializer(serializers.ModelSerializer):
    stock =  serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
    # category = CategorySerializer()
    class Meta:
        model = MenuItem
        fields = ['id','title','price','stock', 'price_after_tax','category']
        depth = 1
    
    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)
```

Tenga en cuenta la línea comentada, category = CategorySerializer() . Y la nueva línea, depth = 1 , se agregó en la clase Meta. Ahora, si visitara el punto final de los elementos del menú en http://127.0.0.1:8000/api/menu-items , notaría que el resultado es exactamente el mismo que antes.

Mostrar campos anidados de esta manera proporciona más información. También reduce la cantidad de código que los desarrolladores de aplicaciones cliente necesitan escribir. Esto se debe a que ya no tienen que realizar llamadas a la API por separado para recuperar los detalles de esos campos anidados.

A continuación, centrémonos en las diferentes técnicas de serialización que puede usar para mostrar campos de modelos relacionados como hipervínculos.


## Mostrar un campo de campos de modelo relacionado como un hipervínculo


En DRF puede mostrar cada campo de modelo relacionado como un hipervínculo en la salida de la API. Así:   http://127.0.0.1:8000/api/category/{categoryId}   para el campo de categoría. Hay dos maneras diferentes de hacer esto. El primer método es usar el campo del serializador llamado HyperlinkedRelatedField y para el segundo método usa el HyperlinkedModelSerializer .

### Método 1: campo relacionado hipervinculado  
#### **Paso 1: Crear y mapear una nueva función de vista**

Cada campo HyperlinkedRelatedField en un serializador necesita un conjunto de consultas para encontrar el objeto relacionado y un nombre de vista que se usa para asignar el patrón de URL con hipervínculo.

Por lo tanto, debe crear una nueva función en el archivo views.py que manejará los puntos finales de categoryId .

```python
from .models import Category from .serializers import CategorySerializer
@api_view()
def category_detail(request, pk):
    category = get_object_or_404(Category,pk=pk)
    serialized_category = CategorySerializer(category)
    return Response(serialized_category.data) 
```

Luego asigna esta función en el archivo urls.py con un nombre de vista.

```python

path('category/<int:pk>',views.category_detail, name='category-detail')

```

**Sugerencia**: hay una convención que debe seguir al crear este nombre de vista. La regla es que debe agregar -detail después del nombre del campo relacionado, que es **categoría** en `MenuItemSerializer` . Esta es la razón por la que el nombre de la vista era `category_detail` en este código. Si el nombre del campo relacionado fuera usuario , el nombre de la vista sería usuario-detalle

#### **Paso 2: Cree un HyperLinkedRelatedField en el serializador**

El siguiente paso es cambiar el código de MenuItemSerializer . El siguiente código establece el campo de categoría como HyperLinkedRelatedField en el serializador MenuItem .

```python
from .models import Category
class MenuItemSerializer(serializers.ModelSerializer):
    stock =  serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
    category = serializers.HyperlinkedRelatedField(
        queryset = Category.objects.all(),
        view_name='category-detail'
    )
    class Meta:
        model = MenuItem
        fields = ['id','title','price','stock', 'price_after_tax','category']    
    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)
```

Observe cómo se proporcionan un `queryset` y un nombre de vista en la categoría `HyperlinkedRelatedField` . El código sigue la convención para que pueda eliminar la línea view_name='category-detail . Solo es necesario si no siguió la convención y creó el nombre de la vista de una manera diferente en el archivo urls.py.

#### **Paso 3: Agregar contexto**

El paso final es agregar contexto a MenuItemSerializer en la función menu_items , como se muestra a continuación.

```python

serialized_item = MenuItemSerializer(items, many=True, context={'request': request})

```

Nota : El argumento context={'request': request} permite que el extremo de los elementos del menú muestre el campo de categoría como un hipervínculo.

![Alt text](image-2.png)

Puede hacer clic en ese hipervínculo y verificar los detalles de la categoría.

![Alt text](image-3.png)

### Método 2: HyperlinkedModelSerializer

Pero hay otra forma de mostrar un campo de categoría como un hipervínculo. Con este método, debe cambiar el código en el archivo serializers.py . para que MenuItemSerializer amplíe la clase serializers.HyperlinkedModelSerializer en lugar de la clase serializers.ModelSerializer .

```python
class MenuItemSerializer(serializers.HyperlinkedModelSerializer):
    stock =  serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
 
    class Meta:
        model = MenuItem
        fields = ['id','title','price','stock', 'price_after_tax','category']
    
    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)

```

Cuando usa `HyperlinkedModelSerializer` , la salida del extremo de los elementos del menú produce la misma salida con un campo de categoría con hipervínculo como en la captura de pantalla del Método 1, pero el código es mucho más limpio y simple.

Nota : cuando usa un HyperlinkedModelSerializer , aún necesita el patrón de URL con un nombre de vista como lo hizo en la sección anterior. 


```python
urlpatterns = [ 
    path('menu-items',views.menu_items),
    path('menu-items/<int:id>',views.single_item),
    path('category/<int:pk>',views.category_detail, name='category-detail')
]
```

Conclusión
---

En esta lectura, aprendió a mostrar automáticamente un campo de modelo anidado usando la opción de profundidad del serializador. También aprendió a mostrar un campo relacionado como un hipervínculo mediante HyperlinkedRelatedField y HyperlinkedModelSerializer 

