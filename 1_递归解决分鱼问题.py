def fish(n):
    while True:
        z = n
        x = (z * 5 + 1) % 4
        for i in range(4):
            if x != 0:
                break
            z = (z * 5 + 1) / 4
            x = (z * 5 + 1) % 4
        else:
            break
        n += 1
    return z * 5 + 1

print(fish(1))