''' 
Declaraciones de importación: 
    1. Importar el paquete python json incorporado
    2. De employee.py, importar la función details y las variables employee_name, age, title
'''
### WRITE IMPORT STATEMENTS HERE
import json
from employee import details, employee_name, age,title


def create_dict(name, age, title):
    """ Crea un diccionario que almacena la información de un empleado

    [IMPLEMENTO ME]
        1. Devuelve un diccionario que asigna "nombre" a nombre, "edad" a edad, y "título" a título

    Args:
        nombre: Nombre del empleado
        edad: Edad del empleado
        título: Título del empleado

    Devuelve:
        dict - Un diccionario que asigna "nombre", "edad" y "título" a los
               nombre, edad y título, respectivamente. Asegúrese de que 
               que los valores son tipificados correctamente (nombre - cadena, edad - int, 
               título - cadena)
    """
    ### WRITE SOLUTION HERE
    d={"first_name":name,"age":int(age),"title":title}
    return d
    raise NotImplementedError()

def write_json_to_file(json_obj, output_file):
    """ Escribir la cadena json en el archivo

    [IMPLEMENTO ME]
        1. Abrir un nuevo archivo definido por archivo_salida
        2. Escribir json_obj en el nuevo archivo

    Args:
        json_obj: cadena json que contiene la información del empleado
        output_file: el archivo en el que se escribe el json
    """
    ### WRITE SOLUTION HERE
    newfile=open(output_file,'w')
    newfile.write(json_obj)
    newfile.close()
    return newfile

    raise NotImplementedError()

def main():
    # Print the contents of details() -- This should print the details of an employee
    details()

    # Create employee dictionary
    employee_dict = create_dict(employee_name, age, title)
    print("employee_dict: " + str(employee_dict))

    ''' 
    Use a function called dumps from the json module to convert employee_dict
    into a json string and store it in a variable called json_object.
    '''
    ### WRITE YOUR CODE BY MODIFYING THE LINE BELOW
    # In the line below replace the None keyword with your code. 
    # The format should look like: variable = json.dumps(dict)
    
    json_object = json.dumps(employee_dict)
    print("json_object: " + str(json_object))

    # Write out the json object to file
    write_json_to_file(json_object, "employee.json")

if __name__ == "__main__":
    main()
