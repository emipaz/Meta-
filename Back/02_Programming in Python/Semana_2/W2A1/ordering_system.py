menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee', 
        "price": 2.50},
    3: {"name": 'cake', 
        "price": 2.79},
    4: {"name": 'soup', 
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}

def calculate_subtotal(order):
    """ Calcula el subtotal de un pedido

    [IMPLEMENTO ME] 
        1. Suma los precios de todos los artículos del pedido y devuelve la suma

    Args:
        order: lista de dicts que contienen un nombre de artículo y un precio

    Devuelve:
        float = La suma de los precios de los artículos del pedido
    """
    print('Calculating bill subtotal...')
    ### WRITE SOLUTION HERE
    suma = 0
    for pedido in order:
        suma += pedido["price"]
    return round(suma,2)

    raise NotImplementedError()

def calculate_tax(subtotal):
    """ Calcula el impuesto de un pedido

    [IMPLEMENTO ME] 
        1. Multiplica el subtotal por el 15% y devuelve el producto redondeado a dos decimales.

    Args:
        subtotal: el precio para obtener el impuesto de

    Devuelve:
        float - El impuesto requerido de un subtotal dado, que es el 15% redondeado a dos decimales.
    """
    print('Calculating tax from subtotal...')
    ### WRITE SOLUTION HERE
    return round(subtotal * 0.15 , 2 )
    raise NotImplementedError()

def summarize_order(order):
    """ Resume la orden

    [IMPLEMENTO ME]
        1. Calcula el total (subtotal + impuestos) y lo almacena en una variable llamada total (redondeado a dos decimales)
        2. Almacena sólo los nombres de todos los artículos del pedido en una lista llamada nombres
        3. Devolver los nombres y el total.

    Args:
        order: lista de dicts que contienen un nombre de artículo y un precio

    Devuelve:
        tuple de nombres y total. La sentencia de retorno debe ser como 
        
        devolver nombres, total

    """
    print_order(order)
    ### WRITE SOLUTION HERE
    subtotal = calculate_subtotal(order)
    impuesto = calculate_tax(subtotal)
    total    = subtotal + impuesto
    nombres  = [item["name"] for item in order] 
    return nombres , round(total,2)

    raise NotImplementedError()

# This function is provided for you, and will print out the items in an order
def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order

# This function is provided for you, and will display the menu
def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()

# This function is provided for you, and will create an order by prompting the user to select menu items
def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' + str(count) + ' (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order

'''
Here are some sample function calls to help you test your implementations.
Feel free to change, uncomment, and add these as you wish.
'''
def main():
    order = take_order()
    print_order(order)

    # subtotal = calculate_subtotal(order)
    # print("Subtotal for the order is: " + str(subtotal))

    # tax = calculate_tax(subtotal)
    # print("Tax for the order is: " + str(tax))

    # items, subtotal = summarize_order(order)

if __name__ == "__main__":
    main()
