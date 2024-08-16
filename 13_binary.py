num=13
ans=0
position=1
while num!=0:
    rem=num%2
    ans=ans+(rem*position)
    position*=10
    num//=2
print(ans)