from typing import List


def is_report_safe(report):
    # Calculate differences between adjacent levels
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    # Check if all differences are within the range [1, 3] or [-3, -1]
    if not all(1 <= diff <= 3 or -3 <= diff <= -1 for diff in differences):
        return False

    # Check if the report is monotonic (either all increasing or all decreasing)
    is_increasing = all(diff > 0 for diff in differences)
    is_decreasing = all(diff < 0 for diff in differences)

    return is_increasing or is_decreasing


def count_safe_reports(reports):
    safe_count = 0
    for report in reports:
        if is_report_safe(report):
            safe_count += 1
    return safe_count


def count_safe_reports_with_dampener(reports: List[List[int]]):
    safe_count = 0
    for report in reports:
        # If the report is safe, count it as safe
        if is_report_safe(report):
            safe_count += 1
        else:
            # If the report is unsafe, try removing each level
            for i, _ in enumerate(report):
                modified_report = report[:i] + report[i + 1 :]
                if is_report_safe(modified_report):
                    safe_count += 1
                    break  # Stop checking after finding one safe modification
    return safe_count


with open("./data.txt", "r") as file:
    reports = [
        [int(level) for level in report.split(" ")] for report in file.readlines()
    ]
    print(count_safe_reports(reports))
    print(count_safe_reports_with_dampener(reports))
