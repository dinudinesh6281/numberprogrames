num=9
fa_count=0
for fa in range(1,num+1):
    if num%fa==0:
        fa_count+=1
if fa_count==2:
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")
