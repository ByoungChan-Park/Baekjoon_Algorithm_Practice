num_list = []
for number in range(3):
    num_list.append(int(input()))

multiply = str(num_list[0]*num_list[1]*num_list[2])

cnt_list = [0]*10

for i in multiply :
    cnt_list[int(i)] += 1

for i in cnt_list :
    print(i)