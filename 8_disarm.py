num=153
copy=num
ans=0
count=len(str(num))
while num!=0:
    ld=num%10
    ans=ans+(ld)**count
    num//=10
    count-=1
if copy==ans:
    print(f"{copy} is disarm number")
else:
    print(f"{copy} is not disarm number")

    