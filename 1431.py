from math import ceil

days = ["Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"]

months = {"September": 30, "October": 31,
          "November": 30, "December": 31}

first_sep = input()
month_match, day_match = input().split()
a, b = map(int, input().split())
day_match = int(day_match)

days_btw = -2
for key, value in months.items():
    if key != month_match:
        days_btw += value
    else:
        days_btw += day_match
        break

weeks = days_btw // 7
add_days = days_btw % 7
ceiled_weeks = ceil(days_btw / 7)
count = 0

for big in range(8 - add_days):
    for small in range(add_days + 1):
        amount = big * weeks + small * ceiled_weeks
        if a <= amount <= b and count == 0:
            count = amount
            print(big + small)
            i = days.index(first_sep) + 1
            if small > 0:
                print(*(2 * days)[i:(i + small)], sep='\n')
            if big > 0:
                print(*(2 * days)[(i + add_days):
                                  (i + add_days + big)], sep='\n')

if count == 0:
    print("Impossible")