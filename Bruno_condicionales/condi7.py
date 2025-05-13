a = int(input("Ingrese el 1er numero de la funcion cuadratica"))
b = int(input("Ingrese el 2do numero de la funcion cuadratica"))
c = int(input("Ingrese el 3er numero de la funcion cuadratica"))

d = b**2-4*a*c
if d > 0:
    x= ((-b)+d**0.5)/2*a
    xx= ((-b)-d**0.5)/2*a
    print("Las raices reales son ",x,xx)
else:
    print("Error")
