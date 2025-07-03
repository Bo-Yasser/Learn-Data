class Solution(object):
    def removeStars(self, s):
        l = []
        for ch in s:
            if ch != "*":
                l.append(ch)
            
            if ch == "*":
                l.pop()
        
        return "".join(l)
    
s = "leet**cod*e"
b = Solution()
print(b.removeStars(s))

# # reverse star effect : حذف العنصر الذي يلي النجمة وهذا عكس المطلوب 
# class Solution(object):
#     def removeStars(self, s):
#         l = []
#         stars = 0
#         for ch in s:
#             if ch != "*":
#                 if stars > 0:
#                     stars -= 1
#                     continue
#                 else:
#                     l.append(ch)
            
#             if ch == "*":
#                 stars += 1
        
#         return "".join(l)
    
