# class Solution(object):
#     def decodeString(self, s):
#         str_stack = []
#         for ch in s:
            
#             # only status can add elements and we never add the "]" to stack in any step of code cause we dont need
#             if ch != "]":
#                 str_stack.append(ch)

#             # current char equal > ] 
#             else:
#                 # to grouping one substring for case if string size is one we wouldnt need loop 
#                 # but if they more than one char we shuold use loop to group chars together 
#                 sub_str = ""    
#                 while str_stack[-1] != "[":
#                     sub_str = str_stack.pop() + sub_str     # a way to reserve str and this what we need we need this cause pop or LIFO will reserve str
#                 str_stack.pop()

#                 # To grouping the current repeating numbers for case if number size bigger than one number
#                 n = ""         
#                 while str_stack and str_stack[-1].isdigit():
#                     n = str_stack.pop() + n                 # also way to reserve str we need this cause pop or LIFO will reserve str

#                 str_stack.append(int(n) * sub_str)          # finally append repeating char to str_stack with the right order


#         return "".join(str_stack)



class Solution(object):
    def decodeString(self, s):
        str_stack = []
        count_stack = []
        curr_num = 0
        curr_str = ""
        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)

            elif ch == "[":
                str_stack.append(curr_str)
                count_stack.append(curr_num)
                curr_num = 0
                curr_str = ""
            
            elif ch == "]":
                repeat = count_stack.pop()
                prev_str = str_stack.pop()
                curr_str = prev_str + curr_str * repeat

            else:
                curr_str += ch

        return curr_str






f = Solution()
s = "4[a2[c]]"

print(f.decodeString(s)[0])