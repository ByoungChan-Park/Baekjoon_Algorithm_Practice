syllable_list = list(map(int, input().split()))

if syllable_list == sorted(syllable_list):
    print("ascending")
elif syllable_list == sorted(syllable_list, reverse = True):
    print("descending")
else :
    print("mixed")