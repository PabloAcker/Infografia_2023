class Carro:

    def __init__(self, marca, cilindrada, kilometraje):
        self.marca = marca
        self.cilindrada = cilindrada
        self.kilometraje = kilometraje

    def encender(self):
        print ("bruuuum")

carro = Carro("subaru", 1500, 20000)
carro.encender()

print(f"marca carro1:  {carro.marca}")

carro2 = Carro("Nissan", 300, 0)
print(f"marca carro2:  {carro2.marca}")

print("Hello World")