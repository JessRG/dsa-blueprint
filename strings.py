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

# Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.
#
# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
#
# Example 2:
# Input: s = "cbbd"
# Output: "bb"
#
# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
def longestPalindrome(s: str) -> str:
    longest = ""

    for i in range(len(s)):
        # check odd palindromes
        odd_palindrome = expand_around_center(s, i, i)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome

        # check even palindromes
        even_palindrome = expand_around_center(s, i, i + 1)
        if len(even_palindrome) > len(longest):
            longest = even_palindrome

    return longest

def expand_around_center(s, left:int, right:int):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return s[left + 1: right]
print(longestPalindrome("babad"))

# Palindromic Substrings
# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.
#
# Example 1:
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#
# Example 2:
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#
# Constraints:
# 1 <= s.length <= 1000
# s consists of lowercase English letters.
def countSubstrings(s: str) -> int:
    total_count = 0

    for i in range(len(s)):
        # Odd palindrome check
        total_count += extend_around_center_counter(s, i, i)

        # Even palindrome check
        total_count += extend_around_center_counter(s, i, i + 1)

    return total_count

def extend_around_center_counter(s, left:int, right:int):
    count = 0

    while left >= 0 and right < len(s) and s[left] == s[right]:
        count += 1
        left -= 1
        right += 1

    return count
print(countSubstrings("aaa"))

# String to Integer (atoi)
# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
#
# The algorithm for myAtoi(string s) is as follows:
#
# Whitespace: Ignore any leading whitespace (" ").
# Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
# Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of
# the string is reached. If no digits were read, then the result is 0.
# Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain
# in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1
# should be rounded to 231 - 1.
# Return the integer as the final result.
#
# Note: You must not use any built-in library function that converts a string to a number
# (for example, atoi, stoi, Integer.parseInt, int(), parseInt, Number()). Perform the conversion manually.
# Example 1:
# Input: s = "42"
# Output: 42
#
# Explanation:
# The underlined characters are what is read in and the caret is the current reader position.
# Step 1: "42"(no characters read because there is no leading whitespace)
# Step 2: "42"(no characters read because there is neither a '-' nor '+')
# Step 3: "42"("42" is read in)
#
# Example 2:
# Input: s = " -042"
# Output: -42
# Explanation:
# Step 1: "   -042"(leading whitespace is read and ignored)
# Step 2: "   -042"('-' is read, so the result should be negative)
# Step 3: "   -042"("042" is read in, leading zeros ignored in the result)
#
# Example 3:
# Input: s = "1337c0d3"
# Output: 1337
# Explanation:
# Step 1: "1337c0d3"(no characters read because there is no leading whitespace)
# Step 2: "1337c0d3"(no characters read because there is neither a '-' nor '+')
# Step 3: "1337c0d3"("1337" is read in reading stop because the next character is non - digit)
#
# Example 4:
# Input: s = "0-1"
# Output: 0
# Explanation:
# Step 1: "0-1"(no characters read because there is no leading whitespace)
# Step 2: "0-1"(no characters read because there is neither a '-' nor '+')
# Step 3: "0-1"("0" is read in; reading stops because the next character is a non - digit)
#
# Example 5:
# Input: s = "words and 987"
# Output: 0
# Explanation:
# Reading stops at the first non - digit character 'w'.
#
# Constraints:
# 0 <= s.length <= 200
# s consists of English letters(lower - case and upper - case), digits(0 - 9), ' ', '+', '-', and '.'.
def myAtoi(s: str) -> int:
    ans = 0
    MIN = -2 ** 31
    MAX = 2 ** 31 - 1

    # strip leading whitespaces
    s = s.lstrip()
    if not s:
        return 0

    # check for sign
    sign = 1
    idx = 0
    if s[idx] == '-':
        sign = -1
        idx += 1
    elif s[idx] == '+':
        idx += 1

    # check for digits
    while idx < len(s) and s[idx].isdigit():
        digit = ord(s[idx]) - ord('0')
        ans = (ans * 10) + digit
        idx += 1

    # set the sign of value
    ans *= sign

    # clamp answer to MIN and MAX boundaries
    return max(MIN, min(MAX, ans))
print(myAtoi("1337c0d3"))

# Minimum Window Substring
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every
# character in t (including duplicates) is included in the window. If there is no such substring,
# return the empty string "".
# The testcases will be generated such that the answer is unique.
#
# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
#
# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
#
# Example 3:
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
def minWindow(s: str, t: str) -> str:
    if not s or not t:
        return ""

    # build frequency map of string t
    target_counts = {}
    for c in t:
        target_counts[c] = target_counts.get(c, 0) + 1

    # help keep track of the required characters in the substring
    required_matches = len(target_counts)

    left = 0
    min_len = float('inf')
    best_substring = ""
    for right in range(len(s)):
        # check if current character is in target_counts
        char = s[right]
        if char in target_counts:
            target_counts[char] -= 1

            if target_counts[char] == 0:
                required_matches -= 1

        # set minimum substring as soon as required matches is reached and shrink window
        while required_matches == 0:
            # set our minimum length and best substring
            current_window_len = right - left + 1
            if current_window_len < min_len:
                min_len = current_window_len
                best_substring = s[left: right + 1]

            # shrink window
            left_char = s[left]
            # add left character back to the frequency map and increment required matches if needed
            if left_char in target_counts:
                # If this character was perfectly satisfying its requirement,
                # losing it means we now need it again.
                if target_counts[left_char] == 0:
                    required_matches += 1
                target_counts[left_char] += 1

            left += 1
    return best_substring
print(minWindow("cabwefgewcwaefgcf", "cae"))

# Edit Distance
# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
# You have the following three operations permitted on a word:
# Insert a character
# Delete a character
# Replace a character
#
# Example 1:
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse(replace 'h' with 'r')
# rorse -> rose(remove 'r')
# rose -> ros(remove 'e')
#
# Example 2:
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention(remove 't')
# inention -> enention(replace 'i' with 'e')
# enention -> exention(replace 'n' with 'x')
# exention -> exection(replace 'n' with 'c')
# exection -> execution(insert 'u')
#
# Constraints:
# 0 <= word1.length, word2.length <= 500
# word1 and word2 consist of lowercase English letters.
def minDistance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    # cache to perform memoization (top-down)
    cache = {}

    def dfs(i, j):
        # if word1 is exhausted
        if i == m:
            return n - j
        # if word2 is exhausted
        if j == n:
            return m - i

        # check our cache for current for state at i and j
        if (i, j) in cache:
            return cache[(i, j)]

        # if characters are equal; move to next characters
        if word1[i] == word2[j]:
            cache[(i, j)] = dfs(i + 1, j + 1)
        else:
            # if characters mismatch, consider all 3 possible edit operations
            res = 1 + min(dfs(i, j + 1),  # insert
                          dfs(i + 1, j),  # delete
                          dfs(i + 1, j + 1))  # replace
            cache[(i, j)] = res

        return cache[(i, j)]

    return dfs(0, 0)

def minDistanceTabulation(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    # Initialize a 2D grid of size (m+1) x (n+1) with zeros.
    # cache[i][j] will store the minimum edit distance for word1[0...i-1] and word2[0...j-1].
    cache = [[0] * (n + 1) for _ in range(m + 1)]

    # Base Case 1: If word1 is empty (length 0), transforming it into word2
    # of length j requires exactly j insertions.
    for j in range(n + 1):
        cache[0][j] = j

    # Base Case 2: If word2 is empty (length 0), transforming word1
    # of length i into it requires exactly i deletions.
    for i in range(m + 1):
        cache[i][0] = i

    # traverse cache grid
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # match in both words; assign diagonal cell value
            if word1[i - 1] == word2[j - 1]:
                cache[i][j] = cache[i - 1][j - 1]
            else:
                # If characters mismatch, consider all 3 possible edit operations
                # from previously solved subproblems and take the minimum cost + 1:
                # 1. cache[i][j - 1]  -> Insert a character into word1
                # 2. cache[i - 1][j]  -> Delete a character from word1
                # 3. cache[i - 1][j - 1] -> Replace a character in word1
                cache[i][j] = 1 + min(
                    cache[i][j - 1],    # insert
                    cache[i - 1][j],    # delete
                    cache[i - 1][j - 1] # replace
                )
    # The bottom-right cell contains the final answer for the full lengths of both words.
    return cache[m][n]
# print(minDistance("intention", "execution"))
print(minDistanceTabulation("intention", "execution"))