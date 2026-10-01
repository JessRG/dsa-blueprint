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

# Example 2:
# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]

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

# Example 1:
#
# Input: prices = [7, 1, 5, 3, 6, 4]
# Output: 5
# Explanation: Buy on day 2(price=1) and sell on day 5(price=6), profit = 6 - 1 = 5. Note that buying on day 2 and
# selling on day 1 is not allowed because you must buy before you sell.
#
# Example 2:
#
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
