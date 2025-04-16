#club project
age=int(input("enter your age : "))
if age>=18:
    print("welcome to my club..")
    print("menu card :")
    print("1. noodles : 90")
    print("2. sandwitch : 120")
    print("3. burger : 60")
    order=int(input("order : "))
    match order:
        case 1:print("your noodles is orderd please pay 90 rs")
        case 2:
            print("select sandwitch type..")
            print("1. masal sandwitch")
            print("2. corn sandwitch")
            print("3. chees corn mayo sandwitch")
            order=int(input("order :"))
            match order:
                case 1:print("your  masal sandwitch is orderd please pay 120 rs")
                case 2:print("your  corn sandwitch is orderd please pay 120 rs")
                case 3:print("your  chees corn mayo sandwitch is orderd please pay 120 rs")
                case _:print("enter correct order")
        case 3:print("your burger is orderd please pay 60 rs")
        case _:print("enter correct order")
else:
    print(f"you are not adult please try after {18-age} year")
print("thanks for visiting my club")        