var=17
copy=var
ans=0
while var!=0:
    ld=var%10
    ans=ans*10+ld
    var//=10
if copy!=var:
    fa_count1=0
    for fa in range(1,copy+1):
        if copy%fa==0:
            fa_count1+=1
    if fa_count1==2:
        fa_count2=0
        for fa in range(1,ans+1):
            if ans%fa==0:
                fa_count2+=1
        if fa_count2==2:
            print("emrip number")
        else:
            print("not emrip number")
    else:
        print("not emrip number")
else:
    print("not emrip number")
