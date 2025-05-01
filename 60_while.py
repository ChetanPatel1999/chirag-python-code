#wap to count digit in given number.
num=int(input("enter a num : "))#43545
c=0
while num:
   c+=1
   num=num//10
print(f"count of individual digit :  {c}")   
 