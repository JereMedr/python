from burguer import Burguer

#create burguer
burguer1 = Burguer("BBQ and chesse", 600, False)
burguer2 = Burguer("triple", 850, False)
burguer3 = Burguer("double", 500, False)
burguer4 = Burguer("single", 300, False)
burguer5 = Burguer("lenteja", 400, True)
burguer6 = Burguer("lenteja doble", 500, True)
burguer7 = Burguer("lenteja triple", 800, True)

listBurger = [burguer1, burguer2, burguer3, burguer4, burguer5, burguer6, burguer7]

#method list burguer
def listBurguers():
    print("Lista de Burguer:")
    for b in listBurger:
        print(b.mostrar())
#llamados al metodo
listBurguers()

#get cheaper burguer
def getCheaperBurguer():
    cheaper = listBurger[0]
    for b in listBurger:
        if b.price < cheaper.price:
            cheaper = b
    print(cheaper.mostrar())
#llamados al metodo
getCheaperBurguer()

#filter vegetarian burguer
def filterVegetarianBurguer():
    print("Lista de Burguer vegetarianos:")
    for b in listBurger:
        if b.vegetarian == True:
            print(b.mostrar())
#llamados al metodo            
filterVegetarianBurguer()

#register new burguer
def registerBurguer():
    name = input("Ingrese el nombre del Burguer: ")
    price = int(input("Ingrese el precio del Burguer: "))
    vegetarian = input("Ingrese si es vegetariano (True/False): ")
    if vegetarian == "True":
        vegetarian = True
    else:
        vegetarian = False
    burguer = Burguer(name, price, vegetarian)
    listBurger.append(burguer)
    print("Burguer registrado")
    listBurguers()
#llamados al metodo
registerBurguer()

