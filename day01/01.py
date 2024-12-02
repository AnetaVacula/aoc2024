import numpy as np


def input_parser(filename: str) -> tuple[np.array]:
    """
    Parses columns in input file to two arrays with numbers.
    :return: each column as separate array.
    """
    with open(filename) as file:
        lines = file.readlines()
    array = np.array([[int(n) for n in line.strip("\n").split("   ")] for line in lines])
    arr1, arr2 = np.transpose(array)
    return arr1, arr2


def total_distance_calculator(arrays: tuple[np.array]) -> int:
    """
    Sorts the arrays and calculates total distance between elements.
    :return: soln to aoc2024 puzzle 1 - total distance between locations.
    """
    arr1, arr2 = arrays
    sorted1, sorted2 = np.sort(arr1), np.sort(arr2)
    diff = np.subtract(sorted1, sorted2)
    abs_diff = [abs(n) for n in diff]
    return sum(abs_diff)


def similarity_score(arrays: tuple[np.array]) -> int:
    left_arr, right_arr = arrays
    right_list = list(right_arr)

    score = 0
    for n in left_arr:
        occurrences = right_list.count(n)
        score += n * occurrences
    return score


if __name__ == "__main__":
    test_input = input_parser("example01.txt")
    puzzle_input = input_parser("input01.txt")
    print(total_distance_calculator(test_input))
    print(total_distance_calculator(puzzle_input))
    print(similarity_score(test_input))
    print(similarity_score(puzzle_input))