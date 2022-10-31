# Instrucciones de laboratorio: Clases y métodos abstractos

En esta tarea, creará una clase abstracta para un banco que se utilizará para crear una clase regular para un banco específico.  
Esta clase contendrá la implementación del método abstracto de la clase abstracta.  

 <br>

> ### **Consejos: Antes de empezar**
> #### **Para ver su código y sus instrucciones uno al lado del otro**, seleccione lo siguiente en su barra de herramientas de VSCode:
> - Ver -> Diseño del Editor -> Dos Columnas
> - Para ver este archivo en modo de vista previa, haga clic con el botón derecho en este archivo README.md y `Abrir vista previa`.
> - Seleccione su archivo de código en el árbol de código, que lo abrirá en una nueva pestaña de VSCode.
> - Arrastra tus archivos de código de evaluación a la segunda columna. 
> - ¡Buen trabajo! Ahora puedes ver las instrucciones y el código al mismo tiempo. 
> - ¿Preguntas sobre el uso de VSCode? Por favor, consulte nuestros recursos de apoyo [aquí](https://www.coursera.org/learn/programming-in-python/supplement/2IEyt/visual-studio-code-on-coursera)
> #### **Para ejecutar tu código Python**
> - Selecciona tu archivo Python en el árbol de archivos de Visual Studio Code 
> - Puedes hacer clic con el botón derecho del ratón en el archivo y seleccionar "Ejecutar el archivo Python en la terminal" 
> o ejecutar el archivo utilizando el botón de   
    botón de reproducción en la esquina superior derecha 
> de VSCode.  
    (Seleccione "Ejecutar archivo Python en la Terminal" en el botón desplegable proporcionado)
> - Alternativamente, puedes seguir las instrucciones del laboratorio que utilizan comandos de python3 para ejecutar tu código en la terminal.
> 
<br>

## Exercise Instructions

### Instructions

1. Cree una clase llamada `Banco` y pásele `ABC`.  

2. Dentro de la clase tienes que definir dos métodos: 
    - 2.1: Definir una función llamada `basicinfo()` y añadir una sentencia print dentro de ella que diga   
    `"This is a generic bank"` and returning the string `"Generic bank: 0"`. 

    - 2.2: Defina una segunda función llamada `withdraw` y manténgala vacía añadiendo una palabra clave pass debajo de ella.   
   Construya una funcion abstracta agregando el decorador `'@abstractmethod'` justo encima. <br><br>

3. Crea otra clase llamada `Swiss` y pasa la clase `Bank` dentro de ella. 
Esto significa que está heredando de la clase `Banco`. 
    - 3.1: Crear un constructor para esta clase que inicialice una variable de clase `bal` a `1000` <br><br>

4. Reemplaza las dos funciones de la clase Banco: `basicinfo()` and `withdraw()`. 
    - 4.1: Defina una función llamada `basicinfo()` y añada una sentencia de impresión dentro de ella indicando `"This is the Swiss Bank"`  
y devolviendo una cadena con `"Swiss Bank: "` seguido del saldo actual del banco.   
    Por ejemplo, si `self.bal = 80`, entonces devolvería `"Swiss Bank: 80"`

    - 4.2 Defina una segunda función, llamada `withdraw` y pásele un parámetro (aparte de `self):` amount.  
     El importe representa la cantidad que se va a retirar. 

        - 4.2.1: Actualizar la variable de clase bal deduciendo de ella el valor de amount. 
        - 4.2.2: Imprimir el valor de amount dando una salida como: "Withdrawn amount: 30"
        - 4.2.3:  Imprimir el nuevo saldo dando una salida como: "Withdrawn amount: 30"
        - 4.2.4:  Devolver el nuevo saldo
        - Nota: ¡Asegúrese de verificar que hay suficiente dinero para retirar!  
        Si la cantidad es mayor que el saldo, entonces no deduzca ningún dinero de la 
        variable de clase `bal`. En su lugar, imprime una declaración diciendo `"Insufficient funds"`, y devuelve el saldo original de la cuenta en su lugar.

<br>


## Paso final: ¡Envíe su código!
¡Buen trabajo! Para completar esta evaluación:
- Guarda tu archivo a través de Archivo -> Guardar 
- Selecciona "Submit Assignment" en la barra de herramientas del laboratorio. 

Tu código se autocalificará y devolverá la información en breve en la pestaña "Calificaciones".  
También puedes ver tu puntuación en la pestaña "My Submission" de tu Tarea de Programación.
<br> <br> 