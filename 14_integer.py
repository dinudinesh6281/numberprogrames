num=1101
ans=0
power=0
while num!=0:
    ld=num%10
    ans=ans+ld*(2**power)
    power+=1
    num//=10
print(ans)