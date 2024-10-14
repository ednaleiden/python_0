with open("prueba.txt","r") as file:
    for lineas in file:
        print(lineas.strip())


with open("prueba.txt","r") as file:
    lines = file.readlines()
    print(lines)



with open('prueba.txt','a') as file:
    file.write("\n\nBy:Edna")

    
with open('prueba.txt','w') as file:
    file.write("\n\nBy:Edna")
