#wap to check you are eligible casting vote in india or not.
country=input("enter your country : ")
if country=="india":
    age=int(input("enter your age : "))
    if age>=18:
        print("you are eligible for voting")
    else:
         print("you are not eligible for voting")    
else:
    print("you are not indian")