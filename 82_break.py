l1=[12,34,56,78,90]
isFind=False
n=int(input("enter a number : "))
for i in l1:
    if i==n:
        isFind=True
        break
if isFind:
    print("num is found")
else:
    print("num is not found")            
