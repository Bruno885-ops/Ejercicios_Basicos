a = int(input("Ingrese un calculo"))
b = int(input("ingrese v"))
Funcion = {
1 : 100*b,
2 : 100**b,
3 : 100/b
}
c = Funcion.get(a,0)
print(c)