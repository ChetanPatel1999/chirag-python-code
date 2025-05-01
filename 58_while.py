#wap to print sum of individual digit of given number.
num=int(input("enter a num : "))#435
sum=0
while num:
   rem=num%10
   sum=sum+rem
   num=num//10
print(f"sum of individual digit :  {sum}")   
 