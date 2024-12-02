import numpy as np


def total_distance_calculator(filename: str) -> int:
    """
    Parses input file to two arrays with numbers, sorts the arrays
    and calculates total distance between elements.
    :return: soln to aoc2024 puzzle 1 - total distance between locations.
    """
    with open(filename) as file:
        lines = file.readlines()
        array = np.array([[int(n) for n in line.strip("\n").split("   ")] for line in lines])
        arr1, arr2 = np.transpose(array)
        sorted1, sorted2 = np.sort(arr1), np.sort(arr2)
        diff = np.subtract(sorted1, sorted2)
        abs_diff = [abs(n) for n in diff]
        return sum(abs_diff)


if __name__ == "__main__":
    print(total_distance_calculator("example01.txt"))
    print(total_distance_calculator("input01.txt"))
