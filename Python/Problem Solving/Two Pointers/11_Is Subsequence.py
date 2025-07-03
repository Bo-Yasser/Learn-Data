# class Solution(object):
#     def isSubsequence(self, s, t):
#         if len(s) > len(t):
#             return False
        
#         if  len(s) < 1 or s == t:
#             return True

#         sub = 0
#         for i in range(len(t)):
#             if s[sub] == t[i]:
#                 sub += 1
#             if sub == len(s):
#                 return True

#         return False
# s = "abc"
# t = "ahbgdc"

# b = Solution()
# print(b.isSubsequence(s, t))


class Solution(object):
    def isSubsequence(self, s, t):
        if len(s) > len(t):
            return False
        
        if  len(s) < 1 or s == t:
            return True
        
        base = []
        sub = 0
        for i in t:
            if sub < len(s) and i == s[sub]:
                base.append(i)
                sub += 1

        return "".join(base) == s
    

s = "abc"
t = "ahbgdc"

b = Solution()
print(b.isSubsequence(s, t))
