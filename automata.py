f = open("texto.txt", "r")
ver=0
nueva=f.read()
nueva.replace("\n", "")
x=nueva.count("hola")
print(x)
