# Datos de entrada: Lista de diccionarios
employee_list = [
   {"id": 12345, "name": "John", "department": "Kitchen"},
   {"id": 12456, "name": "Paul", "department": "House Floor"},
   {"id": 12478, "name": "Sarah", "department": "Management"},
   {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
   {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
   {"id": 12419, "name": "Gill", "department": "Cashier"}
]

# Función que se pasará a la función map(). No lo cambie.
def mod(employee_list):
   temp = employee_list['name'] + "_" + employee_list["department"]
   return temp

def to_mod_list(employee_list):
   """ Modifica la lista de diccionarios de empleados en lista de cadenas de departamentos de empleados

   [IMPLEMENTO ME] 
      1. Utiliza el método map() para aplicar mod() a todos los elementos de employee_list

   Args:
      lista_de_empleados: lista de objetos de empleados

   Devuelve:
      list: una lista de cadenas formada por nombre + departamento.
   """
   ### WRITE SOLUTION CODE HERE 
   return list( map ( mod , employee_list ) )
   raise NotImplementedError()

def generate_usernames(mod_list):
   """ Genera una lista de nombres de usuario 

   [IMPLEMENTO ME] 
      1. Utiliza la comprensión de la lista y la función replace() para sustituir los espacios
         por guiones bajos

      La comprensión de la lista tiene el siguiente aspecto
      list = [ function() for <item> in <list> ]

      El formato de la función replace() es

      test_str.replace("a", "z") # reemplaza cada "a" en test_str con "z"

   Args:
      mod_list: lista de cadenas de departamentos de empleados

   Devuelve:
      list: una lista de nombres de usuario formada por nombre + departamento delimitados por guiones bajos.
   """
   ### WRITE SOLUTION CODE HERE
   return [i.replace(" ","_") for i in mod_list]

   raise NotImplementedError()

def map_id_to_initial(employee_list):
   """ Asigna el ID del empleado a la primera inicial

   [IMPLEMENTO ME] 
      1. Utiliza la comprensión del diccionario para asignar el id de cada empleado (valor) a la primera letra de su nombre (clave)

      La comprensión del diccionario tiene el siguiente aspecto:
      dict = { key : value for <item> in <list> }

   Args:
      lista_de_empleados: lista de objetos de empleados

   Devuelve:
      dict: un diccionario que mapea el id de un empleado (valor) con su primera inicial (clave).
   """
   ### WRITE SOLUTION CODE HERE
   return { i["name"][0] : i["id"]  for i in employee_list }
   raise NotImplementedError()

def main():
   mod_emp_list = to_mod_list(employee_list)
   print("Modified employee list: " + str(mod_emp_list) + "\n")

   print(f"List of usernames: {generate_usernames(mod_emp_list)}\n")

   print(f"Initials and ids: {map_id_to_initial(employee_list)}")

if __name__ == "__main__":
   main()