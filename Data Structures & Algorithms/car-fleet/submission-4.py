class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        c = [(p,s) for p,s in zip(position,speed)]
        c.sort(key= lambda x : x[0], reverse=True)
        for car in c: 
            t_target = (target-car[0])/car[1]
            if len(stack)==0 or t_target >stack[-1]:
                stack.append(t_target)
            

        return len(stack)

