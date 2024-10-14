#Funciones Lambda programacion funcional
#funciones anoniumas

add = lambda a , b: a + b

print(add(10,4))


numbers = range(11)


squared_numbers = list(map(lambda x : x**2, numbers))
print(squared_numbers)


#pares

even_numbers = list(filter(lambda x: x%2 ==0, numbers))
print(even_numbers)
