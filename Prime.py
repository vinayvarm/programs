num = int(input("enter your number"))
if num > 1:
    for i in range(2, num):
        print(num % i, num, i)
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")


else:
    print(num, "is not a prime number")