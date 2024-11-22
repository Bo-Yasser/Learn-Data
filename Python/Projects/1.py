class Calculater:
    
    opearator = input("Enter Operator =>")
    
    def __init__(self):
        pass
        
    def add(self, *nums):

        
        while len(nums) > 0:
            result = nums[0]
            result = int(input("Enter Number =>"))
            
            for n in nums[1:]:
                result += n
            return result
            
    
    def sub(self, *nums):
        result = nums[0]
        for n in nums[1:]:
            result -= n
        return result       
        
        
    def multi(self, *nums):
        result = nums[0]
        for n in nums[1:]:
            result *= n
        return result        

    def div(self, *nums):
        result = nums[0]
        for n in nums[1:]:
            result /= n
        return result

    

calcu = Calculater()







print(calcu.add())

