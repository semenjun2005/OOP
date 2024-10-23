s = str(input())
counter = 0
min_counter = 0
ans = 0

for i in range(len(s)):
    if s[i] == '(':
        counter += 1
    else:
        counter -= 1
        if counter < min_counter:
            min_counter = counter
            ans = 1
        elif counter == min_counter:
            ans += 1

if counter == 0:
    print(ans)
else:
    print(0)
