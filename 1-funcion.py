import funciones
import time
from funciones import clear 

def suma(number1, number2) :
    total = number1 + number2
    return total

def saludo() :
    nombre ="Dylan"
    print("Hola buenos días")
    print(f"hola { nombre}")
    print("espero esten bien")
        
name = "Dylan"
numero1= 2
numero2 = 2
total = 3
clear()    
saludo()
time.sleep(3)
#print(nombre) aquí no existe la variable, solo dentro de def, que fue ahí donde la declaramos
total = suma(numero1, numero2)
print(total)
print("Salio")