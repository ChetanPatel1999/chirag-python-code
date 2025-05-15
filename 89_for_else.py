#wap to search given number in given table.
n=int(input("enter a number for table: "))#6
s=int(input("enter a number for search: "))#12
for i in range(1,11):
    if s==n*i:
        print("found") 
        break
else:
    print("not found")          
   

