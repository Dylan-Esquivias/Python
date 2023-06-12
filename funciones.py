import os
def separador():
    print("------------------------")
    
def clear():
    if os.name=="posix":
        os.system("clear")
    elif os.name == "ce" or os.name =="nt" or os.name == "dos" :
        os.system("cls")
    print("hola".center(40,"x"))