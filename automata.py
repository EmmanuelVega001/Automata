f = open("texto.txt")
arregloLinea=[]
cadenaCheck=["h","o","l","a"]
cadenaTemporal=[]
ver=0
for line in f:
    for caracter in line :
        arregloLinea.append(caracter)
        for ver in range (4):
            if caracter == "h" and caracter == "o" and caracter == "l" and caracter =="a":
                caractertemp=caracter
                cadenaTemporal.append(caractertemp)
                
print(cadenaTemporal)
