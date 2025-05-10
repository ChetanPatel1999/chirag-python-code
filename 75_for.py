#wap to count factors of givan number.
n=int(input("enter a num : "))
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
print(f"factors count of {n} = {c}")        
