# Lab: Leer datos, almacenar, manipular y enviar nuevos datos a un archivo

En este laboratorio leerás el contenido de un archivo y luego escribirás el contenido en otro archivo.  
Almacenarás el contenido de un archivo en una lista para poder acceder a él de diferentes maneras. 
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

## Esta actividad tiene dos objetivos: 
1. Crear una función para leer un archivo

2. Crear una función para escribir archivos.
 <br><br>


## Exercise Instructions:  
<br>

1. Comprueba que los archivos `sampletext.txt` y `file_ops.py` existen y están presentes dentro de la carpeta del proyecto.   
   Puedes ejecutar el archivo `file_ops.py` abriendo un terminal y ejecutando el siguiente comando:
    ```
    python3 archivo_ops.py 
    ```

2. Completa la función `read_file()` para leer el archivo sampletext.txt utilizando la función `open` y devolver todo el contenido del archivo. 

3. Completar la función `read_file_into_line()` para que devuelva una estructura de datos de todo el contenido del fichero en orden secuencial línea a línea.

4. Completa la función `write_first_line_to_file()` que acepta dos argumentos. Esto debería escribir sólo la primera línea del contenido del archivo en el archivo de salida dado.   

    - **Argumento 1:** El contenido de un fichero a escribir
    - **Argumento 2:** El nombre de un archivo de salida.
<br><br>


5. Completar la función `read_even_numbered_lines()` para devolver una lista de las líneas pares de un fichero (2, 4, 6, etc.) 

6. Completa la función `read_file_in_reverse()` para devolver una lista de las líneas de un fichero en orden inverso. 

<br>

## Paso final: ¡Envíe su código!
¡Buen trabajo! Para completar esta evaluación:
- Guarda tu archivo a través de Archivo -> Guardar 
- Selecciona "Submit Assignment" en la barra de herramientas del laboratorio. 

Tu código se autocalificará y devolverá la información en breve en la pestaña "Calificaciones".  
También puedes ver tu puntuación en la pestaña "My Submission" de tu Tarea de Programación.
<br> <br> 
