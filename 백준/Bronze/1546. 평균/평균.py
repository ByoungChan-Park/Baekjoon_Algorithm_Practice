subject_cnt = int(input())
subject_score = list(map(float, input().split()))

fake_avg = []
for i in subject_score :
    fake_avg.append(i/max(subject_score)*100)

print(sum(fake_avg)/subject_cnt)