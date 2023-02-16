class Vehiculo():
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
    
class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    

tesla = Coche("Gris", 4, 2, 180, "Rx2")
print("\n Color: ",tesla.color ,"\n" ,"Ruedas: ",tesla.ruedas ,"\n" ,"Puertas: ",tesla.puertas ,"\n" ,"Velocidad: ",tesla.velocidad ,"\n" ,"Cilindraje: ",tesla.cilindrada)



