#generadores e iteradores


#crear una lista

my_list = [1,2,3,4]
#obtener iterador

my_iterador = iter(my_list)



#usar iterador
print(next(my_iterador))
#next siver para ver los valores que se van guardando en memori
print(next(my_iterador))
print(next(my_iterador))
print(next(my_iterador))


## generador para iterar yield es como return

def my_genedator():
    yield 1
    yield 2

for value in my_genedator():
    print(value)


def fibonnaci(limit):
    a,b = 0,1
    while a < limit:
        yield a 
        a, b = b , a+b

for num in fibonnaci(10):
    print(num)