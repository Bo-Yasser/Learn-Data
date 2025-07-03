# class Solution(object):
#     def kidsWithCandies(self, candies, extraCandies):
#         max_candy = max(candies)

#         result = []
#         for i in range(len(candies)):
#             a = candies[i] + extraCandies
#             if a >= max_candy:
#                 result.append(True)
#             if a < max_candy:
#                 result.append(False)
#         return result
        
        
        
# candies = [4,2,1,1,2]
# extraCandies = 1

# b = Solution()

# print(b.kidsWithCandies(candies, extraCandies))

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max_candy = max(candies)

        result = []
        for i in candies:

            if i+extraCandies >= max_candy:
                result.append(True)
            else:
                result.append(False)
        
        return result
    
candies = [4,2,1,1,2]
extraCandies = 1

b = Solution()

print(b.kidsWithCandies(candies, extraCandies))