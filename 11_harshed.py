num=12
ans=0
copy=num
while num!=0:
    ld=num%10
    ans+=ld
    num//=10
if copy%ans==0:
    print("harshed number")
else:
    print("not harshed number")
