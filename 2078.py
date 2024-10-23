throws = list(map(int, input().split()))

best_score = sum(throws)
worst_score = sum(throws)

if throws[-2] == 10 and throws[-1] > 20:
    worst_score += 10

for i in range(len(throws)-1):
    if i < len(throws) - 2 and throws[i] == 10:
        if throws[i+1] == 10:
            best_score += min(throws[i+2], 10)
        best_score += min(throws[i+1], 10)
    elif i == len(throws) - 2 and throws[i] == 10:
        best_score += min(throws[i+1], 20)

print(worst_score, best_score)