f = open("texto.txt")
arregloLinea=[]
cadenaCheck=["h","o","l","a"]
cadenaTemporal=[]
ver=0
for line in f:
    for caracter in line :
        cont=0
        arregloLinea.append(caracter)
        caractertemp=caracter
        cadenaTemporal.append(caractertemp)
        
        if arregloLinea[cont] == "h":
            if arregloLinea[cont] == "o":
                if arregloLinea[cont] == "l":
                    if arregloLinea[cont] == "a":
                        ver+=1
    cont+=1           
print(cadenaTemporal)
print (ver)
