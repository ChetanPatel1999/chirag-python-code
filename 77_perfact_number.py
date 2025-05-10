#wap to check given number perfect or not.
n=int(input("enter a num : "))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print("perfact number")    
else :
    print("not perfact number")       
