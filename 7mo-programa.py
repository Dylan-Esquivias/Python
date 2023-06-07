descuento:float= 0
precio : int = int(input("Ingresa el precio de las manzanas: ")) 
cantidad : int = int(input("Ingresa la cantidad de manzanas: "))
if cantidad >=10 :
    descuento = (precio*cantidad)*.10
print("las manzanas están en: " +str (precio))
print(precio)
print("la cantidad es: ")
print(cantidad)
print("Vas a pagar: ")
print((precio * cantidad)-descuento)