with open("./data.txt") as file:
    sum = 0
    lefts = []
    rights = []
    frequency = 0
    for line in file.readlines():
        left, right = line.split(" " * 3)
        lefts.append(int(left))
        rights.append(int(right))

    lefts.sort()
    rights.sort()
    print(len(rights), len(lefts))
    for left, right in zip(lefts, rights):
        sum += abs(int(left) - int(right))
        count = rights.count(left)
        
        frequency += int(left) * count

    with open("./result.txt", "w") as file:
        file.write(f"Sum: {sum}\nFrequency Total: {frequency}")



