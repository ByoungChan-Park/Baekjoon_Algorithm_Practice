num = int(input())
if (num % 4 == 0) & (num % 100 != 0) | (num % 400 == 0) :
    print(1)
else :
    print(0)