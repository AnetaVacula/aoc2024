from copy import deepcopy

def get_reports_as_lists(filename: str) -> list[list[int]]:
    """
    Reads reports from file.
    :param filename:
    :return: list of reports, each containing numerical levels.
    """
    with open(filename) as file:
        return [[int(n) for n in line.strip("\n").split(" ")] for line in file.readlines()]


def all_levels_increasing(report: list[int]) -> bool:
    all_increasing = True
    for i in range(1, len(report) - 1):
        level = report[i]
        left_neighbor = report[i-1]
        right_neighbor = report[i+1]
        is_increasing = left_neighbor < level < right_neighbor
        all_increasing &= is_increasing
    return all_increasing


def all_levels_decreasing(report: list[int]) -> bool:
    all_decreasing = True
    for i in range(1, len(report) - 1):
        level = report[i]
        left_neighbor = report[i-1]
        right_neighbor = report[i+1]
        is_decreasing = left_neighbor > level > right_neighbor
        all_decreasing &= is_decreasing
    return all_decreasing


def all_differences_good(report: list[int]) -> bool:
    all_good = True
    for i in range(1, len(report)):
        level = report[i]
        left_neighbor = report[i-1]
        difference_ok = abs(left_neighbor - level) <= 3
        all_good &= difference_ok
    return all_good


def is_safe(report: list[int]) -> bool:
    return all_differences_good(report) and (all_levels_increasing(report) or all_levels_decreasing(report))


def is_safe_with_dampener(report: list[int]) -> bool:
    safe = False
    for i in range(len(report)):
        dampened_report = deepcopy(report)
        dampened_report.pop(i)
        if is_safe(dampened_report):
            safe = True
    return safe


def count_safe_reports(list_of_reports: list[list[int]]) -> int:
    count = 0
    for report in list_of_reports:
        if is_safe(report):
            count += 1
    return count


def count_safe_with_dampener(list_of_reports: list[list[int]]) -> int:
    count = 0
    for report in list_of_reports:
        if is_safe_with_dampener(report):
            count += 1
    return count


if __name__ == "__main__":
    example_reports = get_reports_as_lists("example.txt")
    my_reports = get_reports_as_lists("input.txt")
    print(count_safe_reports(example_reports))
    print(count_safe_with_dampener(example_reports))
    print(count_safe_reports(my_reports))
    print(count_safe_with_dampener(my_reports))
