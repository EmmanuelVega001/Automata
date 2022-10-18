f = open("texto.txt")
for line in f:
    for caracter in line :
        linea=f.read(1)
        print(linea)
        arregloLinea=[]
        linea.split()
        arregloLinea.append(linea)
        print(arregloLinea)