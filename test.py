num = 2
while num <= 100:
    check = True

    if num == 2:
        check = True
    else:
        test = 2
        while test * test <= num:
            if num % test == 0:
                check = False
            break
        test += 1

    if check:
        print(num)

    num += 1