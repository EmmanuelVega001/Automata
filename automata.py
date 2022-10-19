f = open("texto.txt")
#Creación de arreglos necesarios para hacer la validacion
arregloLinea=[]
cadenaCheck=["h","o","l","a"]
cadenaTemporal=[]
ver=0 #verificacion
for line in f:#Por cada linea del documento
    depuradoLine=line.replace("\n","") #Eliminar los saltos de linea del documento
    for caracter in depuradoLine :
        cont=0 #Contador para la deteccion de numeros
        arregloLinea.append(caracter)#Agregamos al arreglo de la linea todo lo que se encuentra en la linea
        cadenaTemporal.append(caracter)#Arreglo que va a cambiar de estado para verificar si se encuentra la palaba
        if cadenaTemporal[cont] == cadenaCheck[cont]:#Verificamos si el caracter que se busca esta en el arreglo para aceptar
            ver+=1#Aumentamos la verificacion 
    cont+=1#
    cadenaTemporal.clear()
ver/4      
print(cadenaTemporal)
print (int(ver/4))