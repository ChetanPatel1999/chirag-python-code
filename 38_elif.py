# wap to find greatest number between three number.
n1=int(input("enter n1 : "))
n2=int(input("enter n2 : "))
n3=int(input("enter n3 : "))
if n1>n2 and n1>n3:
    print(f"greatest num : {n1}")
elif n2>n3:
    print(f"greatest num : {n2}")
else:
    print(f"greatest num : {n3}")        