c = -1
i= 0 
m = 0
while(c<0) or (i<=0)  or (i>=100) or (m<=0):
    print("Introduce El capital, el interes y el tiempo apropiado")
    c = int(input("Introduce el capital"))
    i = int(input("Introduce el interes"))
    m = int(input("Introduce el tiempo en años"))
    for i in range(m):
        c  = c*(1 + i/100)
    print("Tienes", c," soles")



