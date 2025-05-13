#wap to check given number is prime or not.
n=int(input("enter a num : "))#17
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
    if c>2:
        break    
if c==2:
    print("prime number")    
else :
    print("not prime number")       
