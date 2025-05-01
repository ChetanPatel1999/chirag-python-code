#wap to print reverse number of given number.
num=int(input("enter a num : "))#435
rev=0
while num:
   rem=num%10
   rev=rev*10+rem # 534
   num=num//10
print(f"reverse number : {rev}")   
 