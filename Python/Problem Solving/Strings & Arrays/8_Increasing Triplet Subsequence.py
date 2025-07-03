class Solution(object):
    def increasingTriplet(self, nums):
        first = float("inf")
        second = float("inf")

        if len(nums) < 3:
            return False
        
        for i in nums:
            if i <= first:
                first = i

            elif i <= second:
                second = i
            
            else:
                return True
                
        return False
    


s = Solution()
nums = [2,1,5,0,4,6]
print(s.increasingTriplet(nums))