#diccionario

#almacena clave y valor -diccionario 

#palabra - clave
#concepto - valor

numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers)

del numbers[3]
#acceder en la posicion o extraer informacion llamar la llave
print(numbers[2])

claves = numbers.keys()
print(claves)
#print(type(claves))


values = numbers.values()
print(values)

#clave con valor

pairs = numbers.items()
print(pairs)


contacts = { "Edna" : {
    "apellido": "Dupont",
    "Altura": 1.60,
    "Edad": 25
},
"Andres" :{
    "apellido": "Montealegre",
    "Altura": 1.70,
    "Edad": 28
},
"Itza":{
    "apellido": "Dupont",
    "Altura": 1.50,
    "Edad": 23
}
}
#print(contacts)
print(contacts["Itza"])