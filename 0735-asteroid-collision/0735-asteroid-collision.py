# class Solution:
#     def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#         stack=[]
        
#         for x in asteroids:
#             while stack[-1]>0 and stack and x<0:
#                 if stack[-1]==abs(x):
#                     stack.pop()
#                     x=0                    
#                     break
#                 elif stack[-1]<abs(x):
#                     stack.pop()
#                 else:
#                     x=0
#                     break
#             if x!=0:
#                 stack.append(x)
#             return stack

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for x in asteroids:
            while stack and stack[-1] > 0 and x < 0:
                
                if stack[-1] == abs(x):
                    stack.pop()
                    x = 0
                    break

                elif stack[-1] < abs(x):
                    stack.pop()

                else:
                    x = 0
                    break

            if x != 0:
                stack.append(x)

        return stack




            
                

        