# for-else :- when break is exicute so 
# else is not run. other wise else run.
n=int(input("enter a num : "))#15
for i in range(1,11):
    print(i)
    if i==n:
        break
else:
    print("else run")    