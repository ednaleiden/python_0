to_do = ["hotel",
         "almozar",
         "museo"
         ]

print(to_do)

numbers = [1,2,3,4 , "cinco"]
print(type(numbers))

mix = ["uno", 2,3,4,True,[1,2,3]]
print(mix)
print(len(mix))
print("primer elemento", mix[0])
print("segundo elemento", mix[1])
print("ultimo elemento", mix[-1])
print(mix[2:])
print(mix[2:-2])
mix.append(False)
print(mix)
mix.insert(1,[1,0,5])
print(mix)
print(mix.index([1,0,5]))
numberse = [1,10,2,5,6]
print("Mayor", max(numberse))
print("Menor", min(numberse))
del numberse[-1]
print(numberse)
del numberse[:2]
print(numberse)
del numberse
print(numberse)