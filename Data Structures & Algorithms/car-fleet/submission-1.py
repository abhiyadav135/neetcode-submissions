class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        l=[]
        for i in range(len(position)):
            l.append([position[i],speed[i]])
        l.sort(reverse=True)
        stack=[]
        for i in range(len(l)):
            t=(target-l[i][0])/l[i][1]
            stack.append(t)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
            
        return len(stack)     
        
