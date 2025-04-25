#wap to print even number 1 to n.
n=int(input("enter a num : "))
i=1
print(f"even num 1 to {n} : ",end="")
while i<=n:
    if i%2==0:
        print(i,end=" ")#2 4 6 8
    i+=1
    