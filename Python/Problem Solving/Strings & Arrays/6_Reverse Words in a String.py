# class Solution(object):
#     def reverseWords(self, s):
#         words = []
#         word = ""
#         for char in s:
#             if char != " ":
#                 word += char
            
#             else:
#                 if word != "":
#                     words.append(word)
#                     word = ""

#         if word != "":
#             words.append(word)
        

#         return " ".join(words[::-1])
    
# s = "the sky      is       blue"

# b = Solution()
# print(b.reverseWords(s))



# # 2
# class Solution(object):
#     def reverseWords(self, s):
#         return " ".join(s.split()[::-1])
    



# # 3
# class Solution(object):
#     def reverseWords(self, s):
#         words = []
#         word = ""
#         for char in s:
#             if char != " ":
#                 word += char
            
#             else:
#                 if word != "":
#                     words.append(word)
#                     word = ""

#         if word != "":
#             words.append(word)
        
#         t = len(words) - 1
#         reversed_words = ""
#         while t >= 0:
#             reversed_words += words[t] + " "
#             t -= 1
        
#         return reversed_words
    
# s = "the sky      is       blue"

# b = Solution()
# print(b.reverseWords(s))