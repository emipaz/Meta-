# Import ABC and abstractmethod from the module abc (which stands for abstract base classes)
from abc import ABC, abstractmethod

# Class Bank
class Bank(ABC):
    """ Una clase abstracta de banco

    [IMPLEMENTO ME]
        1. Esta clase debe derivar de la clase ABC
        2. Escriba una función basicinfo() que imprima "Este es un banco genérico" y
           devuelva la cadena "Banco genérico: 0" 
        3. Defina una segunda función llamada retirar y manténgala vacía añadiendo
           añadiendo la palabra clave `pass` debajo de ella. Haz que esta función sea abstracta
           añadiendo una etiqueta "@abstractmethod" justo encima de la declaración de la función.
    """
    ### YOUR CODE HERE
    def basicinfo(self):
        print("This is a generic blank")
        s="Generic bank: 0"
        return s

    @abstractmethod
    def withdraw(self):
        pass

# Class Swiss
class Swiss(Bank):
    """ Un tipo específico de banco que deriva de la clase Banco

    [IMPLEMENTO ME]
        1. Esta clase debe derivar de la clase Banco
        2. Crea un constructor para esta clase que inicialice una variable de clase
           variable `bal` a 1000
        3. Implementar la función basicinfo() para que imprima "Este es el 
           Swiss Bank" y devuelva una cadena con "Swiss Bank: " (no olvide
           el espacio después de los dos puntos) seguido del saldo bancario actual.

           Por ejemplo, si self.bal = 80, entonces devolvería "Swiss Bank: 80"

        4. Implemente la función de retirada de manera que tome un argumento (además de
           self) que es un número entero que representa la cantidad a retirar
           del banco. Deducir el importe retirado del saldo bancario, imprimir 
           el importe retirado ("Importe retirado: {importe}"), imprime el nuevo
           saldo ("Nuevo saldo: {self.bal}"), y devuelve el nuevo saldo.

           Nota: ¡Asegúrese de verificar que hay suficiente dinero para retirar!  
                 Si la cantidad es mayor que el saldo, entonces no deduzca ningún 
                 dinero de la variable de clase `bal`. En su lugar, imprime una 
                 una declaración que diga `"Fondos insuficientes"`, y devuelva el 
                 saldo original de la cuenta.
    """
    ### YOUR CODE HERE
    def __init__(self):
        self.bal=1000
    
    def basicinfo(self):
        print("This is the Swiss Bank")
        s="Swiss Bank: "+str(self.bal)
        return s
    
    def withdraw(self, retiro):
        if( retiro > self.bal):
            print("Insufficient funds")
        else:
            self.bal-= retiro
            print("Withdrawn amount: "+str(retiro))
        print("New Balance: "+str(self.bal))
        return self.bal

# Driver Code
def main():
    assert issubclass(Bank, ABC), "Bank must derive from class ABC"
    s = Swiss()
    print(s.basicinfo())
    s.withdraw(30)
    s.withdraw(1000)

if __name__ == "__main__":
    main()