year = int((input("enter year: ")))

if year % 4 != 0 : #no es divisible entre 4
    print("No es bisisesto")
elif year % 4 == 0 and year % 100 != 0: #divisble entre 4 y no entre 100 o 400
    print("Es bisiesto")
elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0: 
    print("No es bisiesto")
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print("Es bisiesto")