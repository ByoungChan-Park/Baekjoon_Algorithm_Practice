num1, num2 = input().split()

num1_list = []
for i in num1 : 
    num1_list.append(i)

num2_list = []
for i in num2 : 
    num2_list.append(i)

print(max(int(''.join(reversed(num1_list))), int(''.join(reversed(num2_list)))))