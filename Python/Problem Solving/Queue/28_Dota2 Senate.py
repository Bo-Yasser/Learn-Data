class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        
        d_q = []
        r_q = []
        for i, c in enumerate(senate):
            if c == "R":
                r_q.append(i)
            else:
                d_q.append(i)

        while d_q and r_q:
            
            d_index = d_q.pop(0)
            r_index = r_q.pop(0)
            
            if r_index < d_index:
                r_q.append(r_index + len(senate))

            else:
                d_q.append(d_index + len(senate))
            

        return "Radiant" if r_q else "Dire"



# class Solution(object):
#     def predictPartyVictory(self, senate):
#         """
#         :type senate: str
#         :rtype: str
#         """
#         remainingSenate = []
#         countR = 0
#         countD = 0

#         for c in senate:
#             remainingSenate.append(c)

#         # Keep going if either party still exist
#         while 'R' in remainingSenate and 'D' in remainingSenate:
#             current = remainingSenate.pop(0)
#             if current == 'R' and countR == 0:
#                 # Block 'D', nearest D
#                 countD += 1
#                 remainingSenate.append(current)

#             elif current == 'R' and countR != 0:
#                 # 'R' is blocked
#                 countR -= 1
            
#             if current == 'D' and countD == 0:
#                 # Block 'R', nearest R
#                 countR += 1
#                 remainingSenate.append(current)

#             elif current == 'D' and countD != 0:
#                 # 'D' is blocked
#                 countD -= 1

        
#         if 'R' in remainingSenate:
#             return "Radiant"
#         else:
#             return "Dire"
s = Solution()
senate = "RDD"

print(s.predictPartyVictory(senate))

