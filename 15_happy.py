num=19
while num>9:
    d_sum=0
    while num!=0:
        ld=num%10
        d_sum=d_sum+ld**2
        num//=10
    num=d_sum
if num==1 or num==7:
    print("happy number")
else:
    print("not happy number")
    
