num=3456
copy=num
ans=0
count=len(str(num))
while num!=0:
    ld=num%10
    ans=ans+(ld)**count
    num//=10
if copy==ans:
    print(f"{copy} is amstrong")
else:
    print(f"{copy} is not amstrong")

