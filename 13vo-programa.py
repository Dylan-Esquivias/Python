descuento:float= 0
cantidad=int(input("si quieres continuar agrega un número distinto a 0: "))
while cantidad ==0 :
    print("No has vendido nada, adios :)")
    print("a")
    precio : int = int(input("Ingresa el precio de las manzanas: ")) 
    cantidad : int = int(input("Ingresa la cantidad de manzanas: "))
    nombre = input("Inserta tu nombre: ")
    if cantidad == 18 or nombre == "Dylan" :
        descuento = (precio*cantidad)*.20
        descuentoLeyenda = "el descuento es del 20%"
    elif cantidad >= 10 :
        descuento = (precio*cantidad)*.10
        descuentoLeyenda = "el descuento es del 10%"
    else :
        print("No hay descuento") 
    print ("Nota de venta".center(50,"x"))
    print("las manzanas están en: " +str (precio))
    print(precio)
    print("la cantidad es: ")
    print(cantidad)
    print("Vas a pagar: " +str (descuentoLeyenda))
    print((precio * cantidad)-descuento)
