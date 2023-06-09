word = "hola topo"
comprobacionA = comprobacionE = comprobacionI = comprobacionO = comprobacionU = False

for letter in word:
    if "a" in letter.lower() and comprobacionA == False:
        print("a")
        comprobacionA = True