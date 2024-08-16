num=11
copy=num
ans=0
while  num!=0:
    ld=num%10
    ans=ans*10+ld
    num//=10
if copy==ans:
    fa_count=0
    for fa in range(1,ans+1):
        if ans%fa==0:
            fa_count+=1
    if fa_count==2:
        print("palyprime")
    else:
        print("notpaly prime")
else:
    print("not palypprime")
