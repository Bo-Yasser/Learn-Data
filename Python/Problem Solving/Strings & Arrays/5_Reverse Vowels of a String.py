# class Solution(object):
#     def reverseVowels(self, str):

#         v = ["A", "E", "I", "O", "U","a", "e", "i", "o", "u"]
#         str = list(str)
#         chars = [] 
#         for i in str:
#             if i in v:
#                 chars.append(i)
        
#         for a in range(len(str)):
#             if str[a] in v:
#                 str[a] = chars.pop() 
#         return "".join(str)





class Solution(object):
    def reverseVowels(self, s):

        v = set("aeiouAEIOU") 
        
        s = list(s)
        first = 0
        last = len(s) - 1

        while first < last:
            if s[first] not in v:
                first += 1
            elif s[last] not in v:
                last -= 1
            
            else:   
                s[first], s[last] = s[last], s[first]
                first += 1
                last -= 1

        return "".join(s)
    
b = Solution()
s = "IceCreAm"
print(b.reverseVowels(s))