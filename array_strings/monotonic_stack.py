"""
Given an array of integers temperatures representing the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after day i to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0.
"""

from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    result = [0] * n
    stack = []

    # Iterate from right to left (most readable)
    for i in reversed(range(n)):
        current_temp = temperatures[i]

        # (temperature, index)
        while stack and stack[-1][0] < current_temp:
            stack.pop()

        # calculate index
        if stack:
            result[i] = stack[-1][1] - i

        stack.append((current_temp, i))
    return result


if __name__ == "__main__":
    print("ready")
    # Test 1
    assert dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]

    # Test 2
    assert dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]

    # Test 3
    assert dailyTemperatures([30, 60, 90]) == [1, 1, 0]

    # Test 4
    assert dailyTemperatures([90, 80, 70, 60]) == [0, 0, 0, 0]

    print("All tests passed!")

