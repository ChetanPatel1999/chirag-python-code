#wap to print even number 1 to n
n=int(input("enter a num :"))#20
for i in range(1,n+1):
    if i%2==0:
        print(i,end=" ")