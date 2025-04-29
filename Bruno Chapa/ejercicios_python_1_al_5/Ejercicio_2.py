
V = int(input("Ingrese su velocidad en Kilometros por hora: "))
if V < 60:
    print("Esta dentro del limite permitido")
elif V> 60 and V< 81:
    print("Esta en exceso leve, Una factura de 1.000")
else:
    print("Esta en exceso grave, Una multa de 100.000 y auto totalmente retenido")
