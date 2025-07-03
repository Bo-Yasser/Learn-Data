class Solution(object):
    def compress(self, chars):
        write = 0
        read = 0
        while read < len(chars):
            current_char = chars[read]
            count = 0

            while read < len(chars) and chars[read] == current_char:
                count += 1
                read += 1

            chars[write] = current_char
            write += 1
            
            if count > 1:
                for i in str(count):
                    chars[write] = i
                    write += 1
        
        return write
    
chars = ["a","a","b","b","c","c","c"]
s = Solution()
print(s.compress(chars))

