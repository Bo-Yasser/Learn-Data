# class Solution(object):
#     def pivotIndex(self, nums):
#         l_sum = 0
#         r_sum = sum(nums)

#         for r in range(len(nums)):
#             r_sum -= nums[r]

#             if l_sum == r_sum:
#                 return r

#             l_sum += nums[r]
        
#         return -1
# b = Solution()

# nums = [1,7,3,6,5,6]

# print(b.pivotIndex(nums))


# هو هو نفس الحل الاول بس بطريقة اوضح لحساب ال right sum
class Solution(object):
    def pivotIndex(self, nums):
        l_sum = 0
        total_sum = sum(nums)

        for r in range(len(nums)):
            r_sum = total_sum - l_sum - nums[r]

            if l_sum == r_sum:
                return r

            l_sum += nums[r]
        
        return -1

b = Solution()

nums = [1,7,3,6,5,6]

print(b.pivotIndex(nums))

# # O(n2)
# class Solution(object):
#     def pivotIndex(self, nums):

#         for r in range(len(nums)):
#             if sum(nums[0:r]) == sum(nums[r + 1:]):
#                 return r
        
#         return -1