class Solution(object):
    def maxOperations(self, nums, k):
        dict_nums = dict()
        count = 0
        
        for num in nums:

            if num > k:
                continue
            complement = k - num
            if complement in dict_nums and dict_nums[complement] > 0:
                count += 1
                dict_nums[complement] -= 1
            
            else:
                if num in dict_nums:
                    dict_nums[num] += 1
                else:
                    dict_nums[num] = 1
        return count


class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        count =0
        left , right = 0, len(nums)-1

        while left < right:
          summ = nums[left] + nums[right]
          if summ == k:
            count +=1
            left +=1 
            right -=1
          elif summ < k:
            left +=1
          else:
            right -=1
        return count
    
nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
k = 2
b = Solution()

print(b.maxOperations(nums, k))
