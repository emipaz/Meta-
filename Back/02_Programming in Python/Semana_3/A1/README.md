# Instrucciones de laboratorio: Mapeo de valores clave a estructuras de datos de diccionario 

Hasta ahora has aprendido que Python tiene diferentes técnicas para modificar una secuencia de iteradores dada, como una lista o un diccionario, utilizando comprensiones  
la función map(), etc. Ahora vas a utilizar lo que has aprendido. Digamos que tienes una lista de datos de los empleados de la empresa Little Lemon.  
Quieres crear cuentas de acceso para los empleados y crearás nombres de usuario para estos empleados en el primer ejemplo. 

También quiere actualizar la lista de estos empleados en el calendario y quiere acceder fácilmente a sus iniciales y a los ID de los empleados, ya que todos son únicos.  
Para conseguirlo, en el segundo ejemplo, crearás un diccionario con la información necesaria. 
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
 <br><br> 

## Instrucciones para el ejercicio

1. Open the `comprehensions.py` file

2. Implement the `to_mod_list()` function by using the `map()` function to apply `mod()`
   to all elements within `employee_list`.  
    Assign the result of it to a new variable called `map_emp`. Convert `map_emp` to a list and return it. 
   - The `mod()` function returns a string value for example such as `“Lisa_Cold Storage”` from the dictionary passed to it. <br><br>

3. At this point you should have a list of the values such as: `“Lisa_Cold Storage”` mentioned above.  
But that is no good for a username with the whitespace present in it.  
    - Implement the `generate_usernames()` method by using list comprehension and the `replace()` over `mod_list`  
  to replace all spaces `(" ")` with underscores `("_")`. 
    - Return the resulting list. <br><br>

4. We want to create a dictionary that stores employees' first initials and IDs. 
    - Implement `map_id_to_initial()` by using dictionary 
comprehension over the `employee_list` to create a dictionary   
where each key is the 
primera letra del nombre de un empleado y el valor es el ID del empleado.<br><br>

5. Ejecute el script abriendo el terminal y ejecutando el comando:
    ```
    python3 comprehensions.py
    ```

<br>


## Paso final: ¡Envíe su código!
¡Buen trabajo! Para completar esta evaluación:
- Guarda tu archivo a través de Archivo -> Guardar 
- Selecciona "Submit Assignment" en la barra de herramientas del laboratorio. 

Tu código se autocalificará y devolverá la información en breve en la pestaña "Calificaciones".  
También puedes ver tu puntuación en la pestaña "My Submission" de tu Tarea de Programación.
<br> <br> 