p =2 
l= 1000
c= 0

for i in range(p,l):
    pr= True
    j= 2 

while (i>j) and (pr == True):
    if i % j == 0:
        pr= False
        break
    else:
        j= j+1

    if pr == True:
        print(i,"Es primo")
        c= c+1
print("Entre",p, "y",l," hay ",c," n° primos")
