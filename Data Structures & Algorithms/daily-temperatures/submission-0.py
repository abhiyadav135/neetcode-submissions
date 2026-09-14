class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[0]
        ans=[0]*len(temperatures)
        top=stack[-1]
        for i in range(1,len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)    
        return ans            