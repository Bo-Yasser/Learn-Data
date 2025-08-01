# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length



class Solution(object):
    def longestOnes(self, nums, k):
        zeros = 0
        left = 0
        right = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                
                left += 1
            current_len = right - left + 1
            
            if current_len > max_len:
                max_len = current_len

        return max_len



class Solution(object):
    def longestOnes(self, nums, k):

        left = 0
        for right in range(len(nums)):
            k -= 1 - nums[right]

            if k < 0:
                k += 1 - nums[left]
                left += 1
            
        return right - left + 1



                



nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3

b = Solution()
print(b.longestOnes(nums, k))
