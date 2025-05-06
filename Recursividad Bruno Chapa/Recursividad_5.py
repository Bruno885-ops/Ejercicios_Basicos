
a = float(input("Introduce el valor de x"))
e= 1
num = 1 
den = 1
i = 1
num = a**i
den = den*i
i= i+1
e = e + a/den
while not(num/den<0.000001):
    num = a**i
    den = den*i
    i = i + 1
    e = e + num/den
print("e elevado al", a,"es",e)




