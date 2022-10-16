with open('texto.txt') as myfile:
    total_lines = sum(1 for line in myfile )

for line in myfile:
    print("Hola")

