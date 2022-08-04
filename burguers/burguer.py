#create burguer object
class Burguer:
    #__init__ metodo constructor pide parametros para crear un objeto
    def __init__(self, name, price, vegetarian):
        self.name = name
        self.price = price
        self.vegetarian = vegetarian
    #mostrar() metodo que muestra los datos del objeto
    def mostrar(self):
        return self.name + ": " + str(self.price)


# sexo