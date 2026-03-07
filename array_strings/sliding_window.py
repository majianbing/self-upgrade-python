def slidingWindow(input_string: str, target: str) -> str:
    from collections import defaultdict

    if len(target) > len(input_string):
        return ""

    window = defaultdict(int)
    required = defaultdict(int)
    for char in target:
        required[char] += 1

    formed = 0  # Number of unique chars in window with desired frequency
    left = 0
    result = float("inf"), None, None  # (window length, left, right)

    for right in range(len(input_string)):
        char = input_string[right]
        window[char] += 1

        if char in required and window[char] == required[char]:
            formed += 1

        # Try to contract window
        while left <= right and formed == len(required):
            char = input_string[left]

            # Update result if this window is smaller
            if right - left + 1 < result[0]:
                result = (right - left + 1, left, right)

            # Remove character from left
            window[char] -= 1
            if char in required and window[char] < required[char]:
                formed -= 1

            left += 1

    return "" if result[0] == float("inf") else input_string[result[1]:result[2] + 1]

if __name__ == "__main__":
    s = "ADOBECODEBANC"
    target = "ABC"
    print(slidingWindow(s, target))