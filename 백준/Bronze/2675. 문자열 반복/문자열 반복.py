repeat = int(input())
for i in range(repeat):
    num, char = input().split()
    text = ''
    for i in char:
        text += int(num) * i
    print(text)