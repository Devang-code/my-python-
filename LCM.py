print("this is the program for finding LCM")
choose = int(input("enter \n 1. find LCM of two number\n 2.find LCM of three number\n"))
if choose == 0 or choose < 0 or choose > 2:
    print("enter specified values only")
if choose == 1:
    n = 1
    a1 = int(input("enter 1st number"))
    a2 = int(input("enter 2nd number"))
    while n != 0:
        if n % a1 == 0 and n % a2 == 0:
            print(n)
            break
        n += 1

if choose == 2:
    n = 1
    a1 = int(input("enter 1st number"))
    a2 = int(input("enter 2nd number"))
    a3 = int(input("enter 3rd number"))
    while n != 0:
        if n % a1 == 0 and n % a2 == 0 and n% a3 == 0:
            print(n)
            break
        n += 1
