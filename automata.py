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
        cont+=1
    if cadenaTemporal == "h" and cadenaTemporal == "o" and cadenaTemporal == "l" and cadenaTemporal =="a":
            ver+=1
print(cadenaTemporal)
print (ver/4)
