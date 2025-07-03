
# Correct solution but with horriple complexity O(k*n)
# class Solution(object):
#     def maxVowels(self, s, k):
#         # v = set("a", "e", "i", "o", "u")
#         v = "aeiou"
#         max_vowels = 0
#         for i in range(len(s) - k + 1):
#             count = 0
#             for a in range(i, k + i):
#                 if s[a] in v:
#                     count += 1

#             if count > max_vowels:
#                 max_vowels = count
            
#         return max_vowels



class Solution(object):
    def maxVowels(self, s, k):
        v = "aeiou"
        window_vowels = 0
        for g in range(k):
            if s[g] in v:
                window_vowels += 1

        max_vowels = window_vowels
        
        for i in range(k, len(s)):
            if s[i-k] in v:
                window_vowels -= 1

            if s[i] in v:
                window_vowels += 1  

        
            if window_vowels > max_vowels:
                max_vowels = window_vowels
            
        return max_vowels


s = "leetcode"
k = 3

b = Solution()

print(b.maxVowels(s, k))

