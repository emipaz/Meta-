def read_file(file_name):
    """ Lee en un archivo.

    [IMPLEMENTO ME]
        1. Abre y lee el archivo dado en una variable utilizando la función File read()
           función
        2. Imprimir el contenido del archivo
        3. Devolver el contenido del archivo

    Args:
        nombre_fichero: el nombre del fichero a leer

    Devuelve:
        string: contenido del archivo dado.
    """
    ### WRITE SOLUTION HERE
    
    with open(file_name,'r') as file:
        contenido=file.read()
    print(contenido)
    return contenido
    raise NotImplementedError()

def read_file_into_list(file_name):
    """ Lee un archivo y almacena cada línea como un elemento de una lista

    [IMPLEMENTO ME]
        1. Abre el archivo dado
        2. Lee el archivo línea por línea y anexa cada línea a una lista
        3. Devuelve la lista

    Args:
        nombre_fichero: el nombre del fichero a leer

    Devuelve:
        list: una lista donde cada elemento es una línea del fichero.
    """
    ### WRITE SOLUTION HERE
    l=[]
    with open(file_name,'r') as file:
        s=file.readlines()
      
    return s

    raise NotImplementedError()

def write_first_line_to_file(file_contents, output_filename):
    """ Escribe la primera línea de una cadena en un archivo.

    [IMPLEMENTO ME]
        1. Obtiene la primera línea de file_contents
        2. Usa la función File write() para escribir la primera línea en un archivo
           con el nombre de output_filename

        Determinamos que la primera línea es todo lo que hay en una cadena antes del
        primer carácter de nueva línea ('\n').

    Args:
        file_contents: cadena a dividir y escribir en el archivo de salida
        nombre_fichero_de_salida: el nombre del fichero a escribir
    """
    ### WRITE SOLUTION HERE
    s=file_contents.split('\n')[0]
    with open(output_filename,'w') as op:
        op.write(s)
    return 
    raise NotImplementedError()


def read_even_numbered_lines(file_name):
    """ Lee en las líneas pares de un archivo

    [IMPLEMENTO ME]
        1. Abre y lee el archivo dado en una variable
        2. Lee el fichero línea por línea y añade las líneas pares a una lista
        3. Devuelve la lista

    Args:
        nombre_fichero: el nombre del fichero a leer

    Devuelve:
        lista: una lista de las líneas pares del fichero
    """
    ### WRITE SOLUTION HERE
    l=[]
    with open(file_name,'r') as file:
        s=file.readlines()
        c=1
        for i in s:
            if(c%2==0):
                l.append(i)
            c+=1
    return l

    raise NotImplementedError()

def read_file_in_reverse(file_name):
    """ Lee un archivo y devuelve una lista de las líneas en orden inverso

    [IMPLEMENTO ME]
        1. Abre y lee el archivo dado en una variable
        2. Lee el archivo línea por línea y almacena las líneas en una lista en orden inverso
        3. Imprimir la lista
        4. Devolver la lista

    Args:
        nombre_fichero: el nombre del fichero a leer

    Devuelve:
        lista: lista de las líneas del fichero en orden inverso.
    """
    ### WRITE SOLUTION HERE
    l=[]
    with open(file_name,'r') as file:
        s=file.readlines()
    
    return s[::-1]

    raise NotImplementedError()

'''
Aquí tienes algunos comandos de ejemplo para ayudarte a ejecutar/probar tus implementaciones.
Siéntase libre de descomentar/modificar/añadir a ellos como desee.
'''
def main():
    #file_contents = read_file("sampletext.txt")
    print(read_file_into_list("sampletext.txt"))
    #write_first_line_to_file(file_contents, "online.txt")
    #print(read_even_numbered_lines("sampletext.txt"))
    #print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()