import re

# Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
#
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
#
# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = defaultdict(int)

        # Count frequencies in s
        for char in s:
            freq[char] += 1

        # Decrement and check early for t
        for char in t:
            freq[char] -= 1
            if freq[char] < 0:
                return False

        return True

# Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
# non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and
# numbers. Given a string s, return true if it is a palindrome, or false otherwise.
#
# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#
# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non - alphanumeric characters. Since an empty string reads
# the same forward and backward, it is a palindrome.
#
# Constraints:
# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.
def isPalindrome(s: str) -> bool:
    s_str = re.sub(r'[^a-zA-Z0-9]', "", s)
    s_str = s_str.lower()

    left = 0
    right = len(s_str) - 1
    while left < right:
        if s_str[left] != s_str[right]:
            return False
        left += 1
        right -= 1

    return True