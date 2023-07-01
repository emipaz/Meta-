# Instrucciones de laboratorio: Funciones, bucles y estructuras de datos

En este laboratorio se le presentará un sistema de ordenamiento de menús que permitirá a los usuarios   
ingresar tres opciones para un menú selecto. La tarea consiste en completar el sistema de menús para que   
que devuelva y calcule la cuenta final para el usuario.
 <br><br>

> ### **Consejos: Antes de empezar**
> #### **Para ver su código y sus instrucciones uno al lado del otro**, seleccione lo siguiente en su barra de herramientas de VSCode:
> - Ver -> Diseño del Editor -> Dos Columnas
> - Para ver este archivo en modo de vista previa, haga clic con el botón derecho en este archivo README.md y `Abrir vista previa`.
> - Seleccione su archivo de código en el árbol de código, que lo abrirá en una nueva pestaña de VSCode.
> - Arrastra tus archivos de código de evaluación a la segunda columna. 
> - ¡Buen trabajo! Ahora puedes ver las instrucciones y el código al mismo tiempo. 
> - ¿Preguntas sobre el uso de VSCode? Por favor, consulte nuestros recursos de apoyo [aquí](https://www.coursera.org/learn/programming-in-python/supplement/2IEyt/visual-studio-code-on-coursera).
> #### **Para ejecutar tu código Python**
> - Selecciona tu archivo Python en el árbol de archivos de Visual Studio Code 
> - Puedes hacer clic con el botón derecho del ratón en el archivo y seleccionar "Ejecutar el archivo Python en la terminal" 
> o ejecutar el archivo usando el botón de   
    botón de reproducción en la esquina superior derecha 
> de VSCode.  
    (Seleccione "Ejecutar archivo Python en la Terminal" en el botón desplegable proporcionado)
> - Alternativamente, puedes seguir las instrucciones del laboratorio que utilizan comandos de python3 para ejecutar tu código en la terminal.
> 

<br> 

## Esta actividad tiene tres objetivos principales:
1. Crear nuevas funciones para resolver problemas concretos.
2. Adquirir experiencia en el uso de bucles for para iterar sobre diferentes colecciones de datos.
3. 3. Crear y utilizar estructuras de datos para almacenar, recuperar y hacer bucles sobre los datos.

<br>

## Instrucciones para el ejercicio

1. Abra el script ordering_system.py presente dentro de la carpeta del proyecto.

2. Ejecute el script y, cuando se le solicite, introduzca los tres productos de su elección según el menú - 1 = espresso, 2 = café, etc.

3. Para ejecutar el script, abra el terminal y ejecute el siguiente comando. 

    ```
    python3 ordering_system.py
    ```

4. Amplíe el script para tener una nueva función llamada `calcular_subtotal`.  
 Debe aceptar un argumento que es la lista de pedidos y devolver la suma   
 de los precios de los artículos de la lista de pedidos.

5. 5. Implementar `calculate_tax()` que calcula el impuesto del subtotal.   
El porcentaje de impuestos es el 15% del total de la factura.

6. Implementar `summarize_order()` que devuelve una lista con los nombres de los artículos   
que el cliente ha pedido y el importe total (impuestos incluidos) que tiene que pagar.  
 Los pedidos deben mostrar el nombre y el precio.

<br>

## Paso final: ¡Envíe su código!
¡Buen trabajo! Para completar esta evaluación:
- Guarda tu archivo a través de Archivo -> Guardar 
- Selecciona "Submit Assignment" en la barra de herramientas del laboratorio. 

Tu código se autocalificará y devolverá la información en breve en la pestaña "Calificaciones".  
También puedes ver tu puntuación en la pestaña "My Submission" de tu Tarea de Programación.