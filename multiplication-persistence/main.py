count = 0

def check_persistence(n):
    global count
    if len(str(n)) == 1:
        print(f"{initial} has a multiplication persistence of {count}")
        return
    new_num = 1
    for digit in str(n):
        new_num *= int(digit)
    count += 1
    print(new_num)
    check_persistence(new_num)

initial = input("What number's multiplication persistence would you like to check?\n - ")
check_persistence(initial)