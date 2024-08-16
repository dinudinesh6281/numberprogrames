num=121
res=0
copy=num
while num!=0:
    ld=num%10
    res=res*10+ld
    num//=10
if copy==res:
    print(f"{res} is palindrome")
else:
    print(f"{res} is not palindrome")
