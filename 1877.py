first_code, second_code = int(input()), int(input())
thief_code = 0
while thief_code <= 9999:
    if thief_code % 2 == 0:
        if thief_code == first_code:
            print('yes')
            exit()
    else:
        if thief_code == second_code:
            print('yes')
            exit()
    thief_code += 1
print('no')





