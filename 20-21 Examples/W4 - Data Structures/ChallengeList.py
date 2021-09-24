
# TODO: Create a list of numbers, print out whether a number is even or odd

nlist = [4, 10, 12, 1, 4, 5, 9, 10, 11]

for x in nlist:
    ans = x % 2
    if ans == 0:
        print(f"{x} is even.")
    else:
        print(f"{x} is odd.")