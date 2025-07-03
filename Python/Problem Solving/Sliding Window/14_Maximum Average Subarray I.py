class Solution(object):
    def findMaxAverage(self, nums, k):
        window_sum = 0
        for g in range(k):
                    window_sum += nums[g]
        
        max_sum = window_sum

        for i in range(k,len(nums)):
            window_sum = window_sum - nums[i-k] + nums[i]

            if window_sum > max_sum:
                max_sum = window_sum
        
        return float(max_sum) / k
    



nums = [1, 12, -5, -6, 50, 3]
k = 4

b = Solution()

print(b.findMaxAverage(nums, k))

        


        