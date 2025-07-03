class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []

        for curr in asteroids:
            while stack and curr < 0 and stack[-1] > 0:
                if abs(curr) > stack[-1]:
                    stack.pop()
                    continue
                
                elif abs(curr) == stack[-1]:
                    stack.pop()

                break

            else:
                stack.append(curr)

        return stack

asteroids = [8,-8,-8,-8]
v = Solution()

print(v.asteroidCollision(asteroids))

# # Same Code But with alive idea to make it easier 
# class Solution(object):
#     def asteroidCollision(self, asteroids):
#         stack = []

#         for curr in asteroids:
#             alive = True
#             while stack and curr < 0 and stack[-1] > 0:
#                 if abs(curr) > stack[-1]:
#                     stack.pop()
#                     continue
                
#                 elif abs(curr) == stack[-1]:
#                     stack.pop()
#                     alive = False
#                     break
#                 else:
#                     alive = False
#                     break

#             if alive:
#                 stack.append(curr)

#         return stack