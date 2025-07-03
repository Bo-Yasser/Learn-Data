class Solution:
    def gcdOfStrings(self, str1, str2):
        def divides(str, word):
            if len(str) % len(word) != 0:
                return False

            repeat = len(str) // len(word)
            return word * repeat == str
        

        min_len = min(len(str1), len(str2))
        for i in range(min_len, 0, -1):
            word = str1[:i]
            if len(str1) % i == 0 and len(str2) % i == 0:
                if divides(str1, word) and divides(str2, word):
                    return word
        
        return ""

class Solution:
    def gcdOfStrings(self, str1, str2):

        if str1 + str2 != str2 + str1:
            return ""

        a,b = len(str1), len(str2)

        while b:
            a,b = b, a % b

        return str1[:a]
str1 = "LEET"
str2 = "CODE"

b = Solution()

print(b.gcdOfStrings(str1, str2))

