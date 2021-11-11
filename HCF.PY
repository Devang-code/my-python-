print("this is the program for finding HCF")
choose = int(input("enter \n 1. find HCF of two number\n 2.find HCF of three number\n"))
if choose == 0 or choose < 0 or choose > 2:
    print("enter specified values only")
if choose == 1:


    a1 = int(input("enter 1st number"))
    a2 = int(input("enter 2nd number"))
    n = min(a1, a2) - 1
    while n != 0:
        if a1 % n == 0 and a2 % n == 0:
            print(n)
            break
        n -= 1

if choose == 2:

    a1 = int(input("enter 1st number"))
    a2 = int(input("enter 2nd number"))
    a3 = int(input("enter 3rd number"))
    n = min(a1, a2, a3) - 1
    while n != 0:
        if a1 % n == 0 and a2 % n == 0 and a3 % n == 0:
            print(n)
            break
        n -= 1

