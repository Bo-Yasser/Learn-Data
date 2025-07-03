# class Solution:
#     def mergeAlternately(self, word1, word2):
#         word = ""
#         i = 0
#         while i < len(word1) and i < len(word2):
#             word += word1[i]
#             word += word2[i]
#             i += 1
#         word += word1[i:]
#         word += word2[i:]

#         return word
             




# b = Solution()
# word1 = "ab"
# word2 = "pqrs"

# print(b.mergeAlternately(word1, word2))



class Solution:
    def mergeAlternately(self, word1, word2):
        word = ""
        max_len = max(len(word1), len(word2))
        for i in range(max_len):
            if i < len(word1):
                word += word1[i]
            if i < len(word2):
                word += word2[i]
        return word

# b = Solution()
# word1 = "ab"
# word2 = "pqrs"

# print(b.mergeAlternately(word1, word2))


class Solution:
    def mergeAlternately(self, word1, word2):
        ptr_word1 = 0
        ptr_word2 = 0 
        word = ""
        while ptr_word1 < len(word1) and ptr_word2 < len(word2):
            word += word1[ptr_word1]
            word += word2[ptr_word2]

            ptr_word1 += 1
            ptr_word2 += 1

        if len(word1) > len(word2):
            word += word1[ptr_word1:]
        else:
            word += word2[ptr_word2:]

        return word
    

b = Solution()
word1 = "ab"
word2 = "pqrs"

print(b.mergeAlternately(word1, word2))