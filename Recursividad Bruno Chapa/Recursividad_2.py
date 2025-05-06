
print("Introduce un numero y para acabar un numero negativo")


a = int(input("Introduce un numero"))
while a>0:
    s = 0
    for i in range(1,a+1):
        if a % i == 0:
            s = s + i
    print("La suma de los 2 divisores es", s,"\n")
    print("Introduce un numero, y para acabar un numero negativo")
    a = int(input("Introduce un numero"))