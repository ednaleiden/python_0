#bucles o condiciones de control

numbers = [1,2,3,4,5,6]

for i in numbers:
    print(i+1)

for i in range(3,10):
    print(i)

#mientra se cumpla una cndicion

x=0
while x<5 :
    print(x)
    x +=1

# temina
x=0
while x<5 :
    if x == 3:
        break
    print(x)
    x +=1

#omite el valor y continua
    numbers = [1,2,3,4,5,6]

for i in numbers:
    if i == 3:
        continue
    print(i+1)

