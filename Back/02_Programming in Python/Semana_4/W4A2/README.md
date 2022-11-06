Lab Instructions: Write a test

En este ejercicio, aprenderás a crear casos de prueba para un bloque de código dado utilizando PyTest.  

Comprobarás la exactitud de una cadena de entrada a una función dada en función de algunas condiciones y escribirás dos funciones:
- **La primera función** comprobará si la longitud de la cadena de entrada está dentro de un   límite específico de palabras y caracteres. 
- **The second function** will check if the basic grammar of the string is well-defined.
 

> ### **Consejos: ¡Antes de empezar!
> #### **Para ver el código y las instrucciones lado a lado**, seleccione lo siguiente en su barra de herramientas VSCode:
> - View -> Editor Layout -> Two Columns
> - To view this file in Preview mode, right click on this README.md file and `Open Preview`
> - Select your code file in the code tree, which will open it up in a new VSCode tab.
> - Drag your assessment code files over to the second column. 
> - Great work! You can now see instructions and code at the same time. 
> - Questions about using VSCode? Please see our support resources [here](https://www.coursera.org/learn/programming-in-python/supplement/2IEyt/visual-studio-code-on-coursera).
> #### **To run your Python code**
> - Select your Python file in the Visual Studio Code file tree 
> - You can right click the file and select "Run Python File in Terminal" 
> or run the file using the smaller   
    play button in the upper right-hand corner 
> of VSCode.  
    (Select "Run Python File in Terminal" in the provided button dropdown)
> - Alternatively, you can follow lab instructions which use python3 commands to run your code in terminal.
> 

<br>

## Objective of this activity:   
Asegurar que las variables de cadena que se pasarán como argumentos al código tengan una longitud determinada y una estructura bien definida.<br><br>

## Instructions:

1. Abrir el archivo `test_spellcheck.py` dentro de la carpeta del proyecto.

2. Importar los módulos `pytest` y `spellcheck`.
3. Comentar la variable beta usando el símbolo # por ahora. 
4. A continuación, complete las funciones `test_length()` y `test_struc()`.   
Estas dos funciones utilizan input_value para comprobar si las funciones definidas en spellcheck se comportan correctamente. 
5.  En la función `test_length()` debe añadir dos sentencias assert.   
En cada sentencia assert debe llamar primero a la función requerida del fichero spellcheck que ha importado,  
y luego comprobar algunas condiciones. For example, the format will be similar to the following against some condition:
    ```
    assert spellcheck.some_function(input_value)
    ```
- 5.1: Añade la primera sentencia assert sobre `función recuento_de_palabras()` del código principal que afirma que el valor devuelto es menor que 10.
    
- 5.2: Add the second assert statement over `function char_count()` from the main code which asserts that the returned value is less than 50. 
<br><br>

6. En la segunda función `test_struc()`, debes añadir dos sentencias assert. The first assert statement checks if the first character is in upper case.  
La segunda sentencia assert comprueba si la sentencia o la variable de cadena pasada termina con un punto (".") 
- Add the first assert statement over function `first_char()` from the main code.  
Ahora llama a una función incorporada `isupper()` directamente sobre ella, como `función_nombre.isupper()`. 
- `isupper()` devuelve True si se llama sobre un carácter en mayúscula y False si se llama sobre un carácter en minúscula.  
Por ejemplo, `"A".isupper()` devuelve `True` y `"a".isupper()` devuelve `False`.
- Add the segundo assert declaración sobre la función `last_char()`del código principal y compararlo con `"." ` 
<br><br>

7. Save the files.
8. Open the terminal to execute the files.
9. Run the code using the following command (within the project directory):
    ```
    python3 -m pytest test_spellcheck.py 
    ```
10. Both the tests should pass in this case.  


- **BONUS STEP:**<br>
Pase la variable beta en lugar de alfa en las cuatro funciones.  
El resultado debería mostrar ahora una prueba superada y otra fallada.  

<br>

> **Tips**<br>
> Asegúrese de volver a comprobar algunos errores comunes cometidos en este proceso 
  below before submitting!  
> - Olvidarse de importar el archivo de código `pytest` y `main`.
> - No pasar los nombres de las variables correctamente
> 
<br>


## Final Step: Let's submit your code!
¡Buen trabajo! To complete this assessment:
- Guarda tu archivo a través de Archivo -> Guardar 
- Select "Submit Assignment" in your Lab toolbar. 

Su código se autocalificará y devolverá la información en breve en la pestaña "Calificaciones".  
You can also see your score in your Programming Assignment "My Submission" tab.
<br> <br> 