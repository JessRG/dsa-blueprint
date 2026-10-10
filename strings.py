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
def isAnagram(s: str, t: str) -> bool:
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
print(isAnagram(s="anagram", t="nagaram"))

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
import re
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
print(isPalindrome("A man, a plan, a canal: Panama"))

# Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
#
# Example 1:
# Input: strs = ["flower", "flow", "flight"]
# Output: "fl"
#
# Example 2:
# Input: strs = ["dog", "racecar", "car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non - empty.
def longestCommonPrefix(strs: list[str]) -> str:
    min_len = float('inf')

    # Get the smallest string length
    for word in strs:
        min_len = min(min_len, len(word))

    # Loop through letters by index of smallest string length
    i = 0
    while i < min_len:
        char = strs[0][i]
        for s in strs:
            if s[i] != char:
                return s[:i]
        i += 1

    return strs[0][:i]
print(longestCommonPrefix(["flower", "flow", "flight"]))

# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.
#
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
#
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
# Constraints:
# 0 <= s.length <= 105
# s consists of English letters, digits, symbols and spaces.
def lengthOfLongestSubstring(s: str) -> int:
    maxx = 0
    start = 0
    letter_set = set()

    for window_end in range(len(s)):
        while s[window_end] in letter_set:
            letter_set.remove(s[start])
            start += 1
        letter_set.add(s[window_end])
        maxx = max(maxx, window_end - start + 1)

    return maxx
print(lengthOfLongestSubstring("pwwkew"))

# Group Anagrams
# Given an array of strings strs, group the anagrams together.You can return the answer in any order.
#
# Example 1:
# Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
# Explanation:
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
#
# Example 2:
# Input: strs = [""]
# Output: [[""]]
#
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
#
# Constraints:
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagrams_map = defaultdict(list)

    for s in strs:
        freq_arr = [0] * 26
        for ch in s:
            freq_arr[ord(ch) - ord('a')] += 1

        key = tuple(freq_arr)
        anagrams_map[key].append(s)

    return list(anagrams_map.values())
print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# Longest Repeating Character Replacement
# You are given a string s and an integer k. You can choose any character of the string and change it to
# any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing
# the above operations.
#
# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A' s with two 'B's or vice versa.
#
# Example 2:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4. There may exists other ways to achieve
# this answer too.
#
# Constraints:
# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length
def characterReplacement(s: str, k: int) -> int:
    longest = 0
    start = 0
    # frequency array to help keep track of character counts in current window
    counts = [0] * 26

    for end in range(len(s)):
        counts[ord(s[end]) - ord('A')] += 1

        # shrink window when the number of changed characters is greater than k
        while (end - start + 1) - max(counts) > k:
            counts[ord(s[start]) - ord('A')] -= 1
            start += 1

        longest = max(longest, end - start + 1)

    return longest
print(characterReplacement("AABABBA", 1))