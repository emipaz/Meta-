# Instrucciones de laboratorio: Import and Scope

Hasta ahora, has aprendido las diferentes formas en las que puedes usar sentencias import para importar otros archivos, módulos y paquetes de Python.   
También has visto las diferentes maneras en que puedes importar funciones específicas utilizando diferentes formatos de importación.   
En esta tarea aprenderás y practicarás cómo usar import para traer código externo dentro del ámbito directo del proyecto.

 <br>

> ### **Tips: Antés de Empezar**
> #### ** Para ver su código y las instrucciones lado a lado**, seleccione lo siguiente en su barra de herramientas de VSCode:
> - View -> Editor Layout -> Two Columns
> - Para ver este archivo en modo de vista previa, haga clic con el botón derecho en este archivo README.md y `Abrir vista previa`.
> - Seleccione su archivo de código en el árbol de código, que lo abrirá en una nueva pestaña de VSCode.
> - Arrastra tus archivos de código de evaluación a la segunda columna. 
> - ¡Gran trabajo! Ahora puedes ver las instrucciones y el código al mismo tiempo. 
> - ¿Preguntas sobre el uso de VSCode? Por favor, consulte nuestros recursos de apoyo [aquí](https://www.coursera.org/learn/programming-in-python/supplement/2IEyt/visual-studio-code-on-coursera).
> #### **Para ejecutar tu código Python**
> - Selecciona tu archivo Python en el árbol de archivos de Visual Studio Code 
> - Puedes hacer clic con el botón derecho del ratón en el archivo y seleccionar "Ejecutar el archivo Python en la terminal" 
> o ejecutar el archivo usando el botón de   
botón de reproducción en la esquina superior derecha 
> of VSCode.  
( Seleccione "Ejecutar archivo Python en la Terminal" en el botón desplegable proporcionado)
> - Alternativamente, puede seguir las instrucciones del laboratorio que utilizan comandos de python3 para ejecutar su código en la terminal.
> 

<br>

## Exercise Objectives:
- Utilizar la sentencia import para importar un paquete incorporado en Python.
- Use the import statement to call a function present in another Python file. 
<br><br>

## Instrucciones

1.  Abrir el archivo jsongenerator.py presente dentro de la carpeta del proyecto.

2. Importar un paquete incorporado llamado `json`. 
   
3. Importa lo siguiente de un archivo llamado employee.py:
   - A la función llamada `details`. 
   - Variables llamadas `employee_name`, `age` and `title`
<br><br>

4. Implementar la función `create_dict()` que devuelve un diccionario dada la información del empleado.   
Crear y devolver un diccionario con tres pares clave-valor donde:
- Las claves son variables de cadena: `"employee_name`, `age` y `title`
y sus respectivos valores son las variables `nombre_del_empleado`, `edad` y `título` que hemos importado del módulo de empleados. 
    - Be sure to cast the values to the expected types.
<br><br>

5. Utiliza una función llamada `dumps()` del módulo json utilizando la notación de puntos y pásale el diccionario `employee_dict` que hemos creado.   
Devuelve su valor a una variable llamada `json_object`. 

El formato de la misma debería ser el siguiente
    ```
    variable = json.dumps(dict) 
    ```

6. Completa la función `write_json_to_file()`.
    - Use a built-in function called `open()` and pass the `output_file` argument and `“w”` to it.   
Devuelve el valor de esta función a una variable llamada newfile.
- llame una función llamada `write()` sobre esta variable newfile. Pasa la variable `json_object` que creaste en el paso 5 dentro de ella.
- Close este fichero llamando a la función incorporada `close()` directamente sobre newfile. You don’t need to pass any arguments here. 
<br><br>


7. Guardar los archivos

8. Abre la terminal para ejecutar los archivos

9. Ejecute el código utilizando el comando (dentro del directorio del proyecto)
   ```
    python3 jsongenerator.py 
    ```

<br>


## Último paso: ¡Vamos a enviar tu código!
¡Buen trabajo! Para completar esta evaluación:
- Guarda tu archivo a través de Archivo -> Guardar 
- Select "Submit Assignment" in your Lab toolbar. 

Su código se autocalificará y devolverá la información en breve en la pestaña "Calificaciones".  
You can also see your score in your Programming Assignment "My Submission" tab.
<br> <br> 