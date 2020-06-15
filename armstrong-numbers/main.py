for num in range(0, 10000):
    new = 0
    for digit in str(num):
        new += int(digit)**3
    if new == num:
        print(new)
