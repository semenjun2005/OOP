k = int(input()) - 1
bwt = input()

n = len(bwt)

first_column = sorted(bwt)

next_idx = [0] * n
count_last = {}

for i, char in enumerate(bwt):
    if char not in count_last:
        count_last[char] = []
    count_last[char].append(i)

count_first = {}
for i, char in enumerate(first_column):
    if char not in count_first:
        count_first[char] = 0
    next_idx[count_last[char][count_first[char]]] = i
    count_first[char] += 1

original = []
idx = k
for _ in range(n):
    original.append(bwt[idx])
    idx = next_idx[idx]

print(''.join(original[::-1]))


