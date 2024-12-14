import re
from typing import List

regex = re.compile(r"(mul\(\d+,\d+\)|don\'t\(\)|do\(\))")


def evaluate(text: List[str]) -> int:
    return sum(
        [
            eval(val.replace("mul", "").replace(",", "*"))
            for val in text
            if val.strip().startswith("mul")
        ]
    )


def enabled_evaluate(text: List[str]) -> int:
    enabled = True
    sum = 0
    for val in text:
        if val == "don't()" and enabled:
            enabled = False

        if val == "do()" and not enabled:
            enabled = True

        if val.strip().startswith("mul") and enabled:
            sum += eval(val.replace("mul", "").replace(",", "*"))

    return sum


with open("./data.txt", "r") as file:
    text = file.read()
    result = regex.findall(text)
    print(result)
    print(evaluate(result))
    print(enabled_evaluate(result))
