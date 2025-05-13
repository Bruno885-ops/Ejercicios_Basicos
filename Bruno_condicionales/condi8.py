
P =3.1416
a = int(input("Ingrese la opcion de menu 1. Area del triangulo 2.Area del circulo "))
if a  == 1:
    l = float(input("Ingrese el lado del triángulo"))
    e = ( (3 ** 0.5)/ 4) * l**2
    print("\nEl área del triángulo es:", e)
elif a == 2:
    r = float(input("Ingrese el radio del círculo"))
    cc = P * r**2
    print("El área del círculo es:", cc)
else: 
    print("Error")