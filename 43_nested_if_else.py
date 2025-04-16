# wap to find greatest number between three numbers without using logical and operator.
n1=int(input("enter n1 : "))#123
n2=int(input("enter n2 : "))#5666
n3=int(input("enter n3 : "))#899
if n1>n2:
    if n1>n3:
         print(f"greatest num : {n1}") 
    else:
          print(f"greatest num : {n3}") 
else:
    if n2>n3:
          print(f"greatest num : {n2}")  
    else:
          print(f"greatest num : {n3}")                   