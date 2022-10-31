# Usando la conversión explícita de tipos, cambia las siguientes 
# entradas para que los tipos coincidan con los siguientes
#  
# nombre = tipo str
# edad  = tipo int
# altura = tipo float
# lealtad = tipo booleano

# Modificar la línea de abajo
name = input('What is your name? ')

print(f"Type of name variable is: {type(name)}. It should be <class 'str'>")

# Modify the line below
age = int(input('What is your age? '))

print(f"Type of age variable is: {type(age)}. It should be <class 'int'>")

# Modify the line below
height = float(input('What is your height in meters? '))

print(f"Type of height variable is: {type(height)}. It should be <class 'float'>")

# Modify the line below
loyalty = bool(input('Are you part of our loyalty program? '))

print(f"Type of loyalty variable is: {type(loyalty)}. It should be <class 'bool'>")