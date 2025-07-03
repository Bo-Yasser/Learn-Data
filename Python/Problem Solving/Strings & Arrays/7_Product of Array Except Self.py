# Solution with O(n^2)
# class Solution(object):
#     def productExceptSelf(self, nums):
#         l = []
        
#         for a in range(len(nums)):
#             product = 1
#             for g in range(len(nums)):
#                 if a != g:
#                     product *= nums[g]

#             l.append(product)
        
#         return l
    

# b = Solution()
# nums = [1,2,3,4]
# print(b.productExceptSelf(nums))

##############################################################################

# First Solution with O(n)
# class Solution(object):
#     def productExceptSelf(self, nums):
#         n = len(nums)
#         answer = [1] * n

#         prefix = 1
#         for i in range(n):
#             answer[i] = prefix
#             prefix *= nums[i]

#         suffix = 1
#         for a in range(n - 1, -1, -1):
#             answer[a] *= suffix
#             suffix *= nums[a]


#         return answer


# Second Solution with O(n)
# class Solution(object):
#     def productExceptSelf(self, nums):
#         n = len(nums)
#         left = [1] * n
#         right = [1] * n
#         answer = [1] * n

#         for i in range(1, n):
#             left[i] = left[i -1] * nums[i-1]

#         for a in range(n - 2, -1, -1):
#             right[a] = right[a + 1] * nums[a + 1]

#         for g in range(n):
#             answer[g] = left[g] * right[g]
        
#         return answer

##############################################################################

# Solution with division And Care Zeros Problem
class Solution(object):
    def productExceptSelf(self, nums):


        num = 1
        zero_count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                num *= nums[i]
            else:
                zero_count += 1
        if zero_count > 1:
            return [0] * len(nums)
        l = []
        if zero_count == 1:
            for g in range(len(nums)):
                if nums[g] != 0:
                    l.append(0)
                else:
                    l.append(num)
            return l
        
        for a in range(len(nums)):
            l.append(num / nums[a])


        return l
    

b = Solution()
nums = [0,0,1,432,42,12]
print(b.productExceptSelf(nums))