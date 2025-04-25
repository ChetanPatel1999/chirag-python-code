# wap to print sum of 1 to n.
i=1
n=int(input("enter a num : "))
sum=0
while i<=n:
    if i< n:
         print(i,end="+")
    else:
          print(i,end="=")     
    sum+=i#55
    i+=1#11
print(sum)   
