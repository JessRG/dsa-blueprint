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