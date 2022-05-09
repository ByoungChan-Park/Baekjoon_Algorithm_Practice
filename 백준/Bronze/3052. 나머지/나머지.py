A_list = []
for i in range(10) : 
    A_list.append(int(input()))

num_set = set()
for i in A_list:
    num_set.add(int(i) % 42)

print(len(num_set))