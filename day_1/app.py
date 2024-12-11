with open("data.txt") as file:
    sum = 0
    lefts = []
    rights = []
    for line in file.readlines():
        left, right = line.split(" " * 3)
        lefts.append(left)
        rights.append(right)
    lefts.sort()
    rights.sort()
    print(lefts)
    print(rights)
    for left, right in zip(lefts, rights):
        sum += abs(int(left) - int(right))
    print(sum)
    