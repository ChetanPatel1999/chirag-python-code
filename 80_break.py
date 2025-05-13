#wap to search given number in given table.
n=int(input("enter a number for table: "))#6
s=int(input("enter a number for search: "))#12
isFind=False
for i in range(1,11):
    if s==n*i:
        isFind=True
        break
if isFind:
     print("found")  
else:
    print("not found")          
   

