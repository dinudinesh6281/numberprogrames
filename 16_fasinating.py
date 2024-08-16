num=192
check=str(num*1)+ str(num*2)+ str(num*3)
for val in range(1,10):
    if str(val) not in check:
        print("fasinating")
        break
else:
    print("not facinatig")