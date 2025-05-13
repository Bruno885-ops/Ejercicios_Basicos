

a = int(input("Ingrese el costo del articulo"))
b = input("Ingrese la marca del producto")
if a >= 2000 and b == "NOSY":
    p = a * 0.90
    pi = p *0.95
    print("Usted pagara",pi,"Soles")
    if a>= 2000 and b!= "NOSY":
        print("Usted pagara ",p,"Soles")
        if a < 2000 and b== "NOSY":
            pl = a * 0.95
            pr = pl + pl*0.20
            print("Usted pagara",pr,"soles")
        else:
            pc = a*1.20
            print("Usted pagara",pc,)

