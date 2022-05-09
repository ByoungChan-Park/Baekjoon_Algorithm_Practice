hour, min = map(int, input().split())

if hour < 1 :
    if min < 45 : 
        print(23, min+15)
    else :
        print(hour, min-45)
elif min < 45 :
    print(hour-1, min+15)
else : 
    print(hour, min-45)