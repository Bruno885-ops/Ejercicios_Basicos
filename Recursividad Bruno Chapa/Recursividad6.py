
a1 = 1
a2 = 0
an = a1+(2*a2)
c = 0
while an <300:
    a2 = a1
    a1 = an
    an = a1 + (2 * a2)
    c = c + 1
    print("El rango es:", c, "y el resultado es:", an)