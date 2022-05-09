word = input()
alphaList = [chr(c) for c in range(ord('a'), ord('z')+1)]

for i in alphaList :
    if i in word : 
        print(word.index(i), end = ' ')
    else :
        print(-1, end = ' ')