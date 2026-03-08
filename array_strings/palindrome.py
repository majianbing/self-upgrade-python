
"""

# Example 1
s = "abca"
Output: True
Reason: Remove 'b' → "aca" is palindrome

# Example 2
s = "abc"
Output: False
Reason: Can't make palindrome even after removing one char

# Example 3
s = "a"
Output: True
Reason: Already a palindrome

# Example 4
s = "ac"
Output: True
Reason: Remove 'a' or 'c' → single char is palindrome

"""




def is_palindrome_range(left :int, right :int, s :str) -> bool:
    while left < right :
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def valid_palindrome(s :str) -> bool:
    # edge cases
    if len(s) <= 2:
        return True

    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return is_palindrome_range(left + 1, right, s) or is_palindrome_range(left, right - 1, s)
        left += 1
        right -= 1

    return True;


if __name__ == "__main__":
    print("start test.")
    print(valid_palindrome("ab"))
    print(valid_palindrome("abc"))
    print(valid_palindrome("abca"))
    print(valid_palindrome("abcda"))

