#wap to check given number is prime or not.
n=int(input("enter a num : "))#23
c=0
for i in range(2,n):
    if n%i==0:
        print("not prime number")  
        break    
else :
    print("prime number")       
