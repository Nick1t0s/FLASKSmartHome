
c=0
for i in range(1,int(math.sqrt(n))+1):
    if (n&i): continue
    c+=1
#        print(f"& {i}")
    if i**2!=n:
        c+=1
#            print(f"2 {i}")