a = int(input("Ingrese un numero"))
par_Impar = {
1 : 'Impar',
3 : 'Impar',
5 : 'Impar',
7 : 'Impar',
9 : 'Impar',
2 : 'Par',
4 : 'Par',
6 : 'Par',
8 : 'Par',
10 : 'Par'
}
print(par_Impar.get(a, "Numero fuera de Rango"))