a = float(input("Ingrese la velocidad del 1er vehiculo"))
b = float(input("Ingrese la velocidad del 2do vehiculo"))
c = float(input("Ingrese la distancia que los separa"))
if  a > 0 and b > 0: 
    t = c/(a+b)
    print("el tiempo de encuentro es en ",t)
else:
    print("ERROR")