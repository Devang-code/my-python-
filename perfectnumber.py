print("this is the program for checking perfect number")
real_num = int(input("enter a number which you want to check\n"))
for num in range(1,real_num + 1):
    add = 0 
    n = num//2 + 1
    for i in range(1,n):
        if num % i == 0:
            add = add + i
    if add == num:
        print(num," is perfect number")
