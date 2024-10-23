f_count = int(input())
extra_friends = 0

for i in range(f_count):
    invite = input()
    if '+one' in invite:
        extra_friends += 1

total = f_count + extra_friends + 2
total = total + 1 if total == 13 else total

print(total * 100)