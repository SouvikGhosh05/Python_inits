x=int(input("Enter the number of quantities: "))

a=[]
b=[]
for _ in range(x):
    y= int(input("Enter the number unit: "))
    z= int(input("Enter the price per unit: "))

    a.append(y)
    b.append(z)
    

c=list(map(lambda a,b : a * b, a, b))
print("Total", sum(c))