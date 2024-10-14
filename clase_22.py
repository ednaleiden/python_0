#manejo de errores try catch

try:
    divisor = int(input("ingrese un numero divisor : "))
    resulr = 100/divisor
    print(resulr)
except:
    print("eldivisor no puede ser 0")