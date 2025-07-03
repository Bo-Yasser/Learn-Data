class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        a= 0
        for i in range(len(flowerbed)):
            
            if flowerbed[i] == 0:
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
                if empty_left and empty_right:
                    flowerbed[i] = 1
                    a += 1
                    if a >= n:
                        return True
        return a >= n



flowerbed = [1,0,0,0,1]
n = 1

b = Solution()
print(b.canPlaceFlowers(flowerbed, n))



# class Solution(object):
#     def canPlaceFlowers(self, flowerbed, n):

#         if len(flowerbed) == 0:
#             if n >= 1:
#                 return False
#             return True
#         if len(flowerbed) == 1:
#             if n == 0:
#                 return True
            
#             if flowerbed[0] == 0 and n <= 1:
#                 flowerbed[0] = 1
#                 return True
            
#             return False      
        
#         num = 0
#         if flowerbed[1] == 0 and flowerbed[0] == 0:
#             num += 1
#             flowerbed[0] = 1
#         if flowerbed[len(flowerbed) - 1] == 0 and flowerbed[len(flowerbed) - 2] == 0:
#             num += 1
#             flowerbed[len(flowerbed) - 1] = 1

#         for i in range(1, len(flowerbed) - 1):
#             if flowerbed[i] == 0:
#                 if flowerbed[i + 1] == 0 and flowerbed[i - 1] == 0:
#                     flowerbed[i] = 1
#                     num += 1
#                     if num >= n:
#                         return True
#         return num >= n




