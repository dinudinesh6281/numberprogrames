num=145
copy=num
res=0
while num!=0:
    id=num%10
    fact=1
    for var in range(1,id+1):
        fact*=var
    res+=fact
    num//=10
if copy==res:
    print("speacial number")
else:
    print("not speacial number")






    