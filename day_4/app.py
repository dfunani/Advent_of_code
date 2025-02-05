with open("./data.txt", "r") as file:
    text = file.readlines()
    count = 0
    for r, row in enumerate(text):
        for c, char in enumerate(row.strip()):
            directions = {
                "forward": [],
                "down": [],
                "diagonal-left": [],
                "diagonal-right": [],
            }
            for direction in directions:
                try:
                    match (direction):
                        case "forward":
                            directions["forward"].append(char)
                            for i in range(1, 4):
                                if (
                                    row[c + i] not in directions["forward"]
                                    and row[c + i] != "\n"
                                ):
                                    directions["forward"].append(row[c + i])
                        case "down":
                            directions["down"].append(char)
                            for i in range(1, 4):
                                if (
                                    text[r + i][c] not in directions["down"]
                                    and text[r + i] != "\n"
                                ):
                                    directions["down"].append(text[r + i][c])
                        case "diagonal-left":
                            directions["diagonal-left"].append(char)
                            for i in range(1, 4):
                                if (
                                    text[r + i][c + i]
                                    not in directions["diagonal-left"]
                                    and text[r + i][c + i] != "\n"
                                ):
                                    directions["diagonal-left"].append(
                                        text[r + i][c + i]
                                    )
                        case "diagonal-right":
                            directions["diagonal-right"].append(char)
                            for i in range(1, 4):
                                if (
                                    text[r + i][c - i]
                                    not in directions["diagonal-right"]
                                    and text[r + i][c - i] != "\n"
                                ):
                                    directions["diagonal-right"].append(
                                        text[r + i][c - i]
                                    )
                except BaseException:
                    pass
            final = {direction: set(array) for direction, array in directions.items() if len(set(array)) == 4}
            if final and all([True for f in final.values() if "".join(f) == "AXMS"]):
                count += 1
    print(count)
