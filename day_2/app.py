import json


with open("./data.txt") as file:
    count = 0
    results = []
    for levels in file.readlines():
        temp = 0
        safe = True
        direction = 0
        for index, level in enumerate(levels.split(" ")):
            if index == 0:
                temp = int(level)
                continue

            diff = abs(int(temp) - int(level))
            if index == 1:
                try:
                    direction = (int(level) - int(temp)) / diff
                except ZeroDivisionError:
                    safe = False
                    break

            if (diff > 3 or (diff == 0 and index != 0)) or direction != (
                int(level) - int(temp)
            ) / diff:
                safe = False
                break

            temp = int(level)

        if safe:
            count += 1
            results.append(levels)

    with open("./result.txt", "w") as file:
        file.write(f"Safes: {count}")

    with open("./result.json", "w") as file:
        json.dump({"Results": results}, file)
