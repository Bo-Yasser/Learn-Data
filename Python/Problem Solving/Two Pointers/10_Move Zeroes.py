class Solution(object):
    def moveZeroes(self, nums):
        left = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[left], nums[r] = nums[r], nums[left]
                left += 1


        return nums


# class Solution(object):
#     def moveZeroes(self, nums):
#         left = 0
#         right = 0
#         while right < len(nums):

#             if nums[right] != 0:
#                 nums[left], nums[right] = nums[right], nums[left]
#                 left += 1
#             right += 1


#         return nums

# class Solution(object):
#     def moveZeroes(self, nums):
#         l =  []
#         zero_count = 0
#         for n in range(len(nums)):
#             if nums[n] != 0:
#                 l.append(nums[n])
#             else:
#                 zero_count += 1
        
#         for i in range(zero_count):
#             l.append(0)
        
#         return l

# Move Zeros to the left
# class Solution(object):
#     def moveZeroes(self, nums):
#         left = len(nums) - 1
#         right = len(nums) - 1
#         while left + 1 > 0:

#             if nums[left] != 0:
#                 nums[right], nums[left] = nums[left], nums[right]
#                 right -= 1
#             left -= 1


#         return nums
# s = Solution()
# nums = [0,1,0,3,12, 0]
# print(s.moveZeroes(nums))