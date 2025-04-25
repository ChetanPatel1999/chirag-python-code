#wap to print factors of given number.
n=int(input("enter a num : "))#15
i=1
print(f"factor of {n} : ",end="")
while i<=n:
    if n%i==0:
        print(i , end=" ")#1 3 5 15
    i+=1    