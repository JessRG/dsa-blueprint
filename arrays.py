from typing import List
# Two Sum
# You are given an array of integers nums and an integer target, return indices of the two numbers
# such that they add up to target. You may assume that each input would have exactly one solution,
# and you may not use the same element twice. You can return the answer in any order.
#
# Example 1:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: Because
# nums[0] + nums[1] == 9, we
# return [0, 1].
#
# Example 2:
# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]
#
# Example 3:
# Input: nums = [3, 3], target = 6
# Output: [0, 1]
#
# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
def twoSum(nums: list[int], target: int) -> list[int]:
    complements = {}
    ans = []

    for i in range(len(nums)):
        if nums[i] in complements:
            ans.append(i)
            ans.append(complements.get(nums[i]))

        complements[target - nums[i]] = i

    return ans

print(twoSum([3,2,4], 6))

# Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction.If you cannot achieve any profit, return 0.
#
# Example 1:
# Input: prices = [7, 1, 5, 3, 6, 4]
# Output: 5
# Explanation: Buy on day 2(price=1) and sell on day 5(price=6), profit = 6 - 1 = 5. Note that buying on day 2 and
# selling on day 1 is not allowed because you must buy before you sell.
#
# Example 2:
# Input: prices = [7, 6, 4, 3, 1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
def maxProfit(prices: list[int]) -> int:
    min_price = float('inf')
    max_profit = float('-inf')

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return int(max_profit)

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))

# Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.
#
# Example 1:
# Input: nums = [1, 2, 3, 1]
# Output: true
# Explanation: The element 1 occurs at the indices 0 and 3.
#
# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: false
# Explanation: All elements are distinct.
#
# Example 3:
# Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# Output: true
#
# Constraints:
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
def containsDuplicate(nums: list[int]) -> bool:
    num_set = set()

    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    return False

print(containsDuplicate([1, 2, 3, 1]))
print(containsDuplicate([1, 2, 3, 4]))
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

# Given an integer array nums, find the subarray with the largest sum, and return its sum.
#
# Example 1:
# Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
# Explanation: The subarray[4, -1, 2, 1] has the largest sum 6.
#
# Example 2:
# Input: nums = [1]
# Output: 1
# Explanation: The subarray[1] has the largest sum 1.
#
# Example 3:
# Input: nums = [5, 4, -1, 7, 8] Output: 23 Explanation: The subarray[5, 4, -1, 7, 8] has the largest sum 23.
#
# Constraints:
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
#
# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer
# approach, which is more subtle.
def maxSubArray(nums: list[int]) -> int:
    if not nums:
        return 0

    max_current, max_global = nums[0], nums[0]

    for element in nums[1:]:
        # calculate the current max sum; start a new subarray if current element is higher
        max_current = max(element, max_current + element)

        # calculate global max subarray
        max_global = max(max_global, max_current)

    return max_global

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([1]))
print(maxSubArray([5, 4, -1, 7, 8]))

# Given an integer array nums, return an array answer such that answer[i] is equal to the product
# of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32 - bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.
#
# Example 1:
# Input: nums = [1, 2, 3, 4]
# Output: [24, 12, 8, 6]
#
# Example 2:
# Input: nums = [-1, 1, 0, -3, 3]
# Output: [0, 0, 9, 0, 0]
#
# Constraints:
# 2 <= nums.length <= 10**5
# -30 <= nums[i] <= 30)
# The input is generated such that answer[i] is guaranteed to fit in a 32 - bit integer.
#
# Follow up: Can you solve the problem in O(1) extra space complexity?
# (The output array does not count as extra space for space complexity analysis.)
def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)
    left_multi = 1
    right_multi = 1
    left_arr = [0] * n
    right_arr = [0] * n
    ans = []

    for i in range(n):
        j = n - 1 - i
        left_arr[i] = left_multi
        right_arr[j] = right_multi
        left_multi *= nums[i]
        right_multi *= nums[j]

    for i in range(n):
        ans.append(left_arr[i] * right_arr[i])

    return ans

print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))

# 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
# and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
#
# Example 1:
# Input: nums = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]
# Explanation: nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0. nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0. The distinct triplets are[-1, 0, 1] and [-1, -1, 2].
# Notice that the order of the output and the order of the triplets does not matter.
#
# Example 2:
# Input: nums = [0, 1, 1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
#
# Example 3:
# Input: nums = [0, 0, 0]
# Output: [[0, 0, 0]]
# Explanation: The only possible triplet sums up to 0.
#
# Constraints:
# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105
def threeSum(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    triplets = []

    # Sort nums array
    nums.sort()
    for i in range(n):
        # Skip duplicate values
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]

            if sum == 0:
                triplets.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                # avoid duplicates on left side
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                # avoid duplicates on right side
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif sum < 0:
                left += 1
            else:
                right -= 1

    return triplets

# Container With Most Water
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints
# of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
#
# Example 1:
# Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# Output: 49
# Explanation: The above vertical lines are represented by array[1, 8, 6, 2, 5, 4, 8, 3, 7].
# In this case, the max area of water(blue section) the container can contain is 49.
#
# Example 2:
# Input: height = [1, 1]
# Output: 1
#
# Constraints:
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104
def maxArea(height: list[int]) -> int:
    n = len(height)
    max_container = 0

    left = 0
    right = n - 1
    while left < right:
        length = min(height[left], height[right])
        width = right - left

        max_container = max(max_container, length * width)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_container

print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))

# Subarray Sum Equals K
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non - empty sequence of elements within an array.
#
# Example 1:
# Input: nums = [1, 1, 1], k = 2
# Output: 2
#
# Example 2:
# Input: nums = [1, 2, 3], k = 3
# Output: 2
#
# Constraints:
# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107
def subarraySum(nums: List[int], k: int) -> int:
    count = 0
    prefix_sum = 0
    prefix_freq_map = {0: 1}

    for num in nums:
        prefix_sum += num

        if (prefix_sum - k) in prefix_freq_map:
            count += prefix_freq_map.get(prefix_sum - k)

        prefix_freq_map[prefix_sum] = prefix_freq_map.get(prefix_sum, 0) + 1

    return count

print(subarraySum([1, 8, 6, 2, 5, 4, 8, 3, 7], 3))
print(subarraySum([2, 3, -5, 5, -5, 1, 4], 5))

# Set Matrix Zeroes
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.
#
# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
#
# Example 2:
# Input: matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
# Output: [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
#
# Constraints:
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1
def setZeroes(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    m = len(matrix)
    n = len(matrix[0])

    has_row_zero = False
    has_col_zero = False

    # Step 1: scan first row for any zeroes
    for c in range(n):
        if matrix[0][c] == 0:
            has_row_zero = True
            break
    # Step 2: scan first column for any zeroes
    for r in range(m):
        if matrix[r][0] == 0:
            has_col_zero = True
            break

    # Step 3: set state trackers on first row/col for inner matrix
    for r in range(1, m):
        for c in range(1, n):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0

    # Step 4: use first row/col as state trackers for inner matrix
    for r in range(1, m):
        for c in range(1, n):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0
    # Step 5: zero out first row if it originally had a zero
    if has_row_zero:
        for c in range(n):
            matrix[0][c] = 0
    # Step6: zero out first col if it originally had a zero
    if has_col_zero:
        for r in range(m):
            matrix[r][0] = 0

    print(matrix)

setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
setZeroes([[1,1,1],[1,0,1],[1,1,1]])

# Spiral Matrix
# Given an m x n matrix, return all elements of the matrix in spiral order.
#
# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
#
# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100
def spiralOrder(matrix: List[List[int]]) -> List[int]:
    result = []
    m = len(matrix)
    n = len(matrix[0]) if matrix else 0
    top = 0
    bottom = m - 1
    left = 0
    right = n - 1

    while left <= right and top <= bottom:
        # Traverse from left to right on top row
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # Traverse from top to bottom on right column
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # Traverse from right to left on bottom row
        # CRITICAL: Since we just updated 'top' and 'right', we must double-check
        # that our boundaries haven't accidentally crossed before moving backward.
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        # Traverse bottom to top on left column
        # CRITICAL: Since we just updated 'top' and 'right', we must double-check
        # that our boundaries haven't accidentally crossed before moving backward.
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    return result

# Trapping Rain Water
# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.
#
# Example 1
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
# In this case, 6 units of rain water (blue section) are being trapped.
def trap(height: list[int]) -> int:
    left_wall = right_wall = 0
    n = len(height)
    max_left = [0] * n
    max_right = [0] * n

    for i in range(n):
        j = n - 1 - i
        max_left[i] = left_wall
        max_right[j] = right_wall
        left_wall = max(left_wall, height[i])
        right_wall = max(right_wall, height[j])

    summ = 0
    for i in range(n):
        water = min(max_left[i], max_right[i])
        summ += max(0, water - height[i])

    return summ

# First Missing Positive
# Given an unsorted integer array nums.Return the smallest positive integer that is not present in nums.
# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
#
# Example 1:
# Input: nums = [1, 2, 0]
# Output: 3
# Explanation: The numbers in the range[1, 2] are all in the array.
#
# Example 2:
# Input: nums = [3, 4, -1, 1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.
#
# Example 3:
# Input: nums = [7, 8, 9, 11, 12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.
#
# Constraints:
# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
def firstMissingPositive(nums: list[int]) -> int:
    n = len(nums)

    # Sort elements to their correct positions
    for idx in range(n):
        while 1 <= nums[idx] <= n and nums[nums[idx] - 1] != nums[idx]:
            correct_idx = nums[idx] - 1
            nums[idx], nums[correct_idx] = nums[correct_idx], nums[idx]

    # Find mismatched element
    for idx in range(n):
        if nums[idx] != idx + 1:
            return idx + 1

    return n + 1