class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping = {')':'(', ']': '[', '}': '{'}
        top=len(stack)-1
        if s==""or len(s)==1:
            return False
        for i in s:
            if i in"[{(":
                stack.append(i)
            elif i in "]})":
                if len(stack)==0:
                    return False
                else:
                    x=stack.pop()
                    top=len(stack)-1
                    if x!=mapping[i]  :
                        return False
        if len(stack)!=0:
            return False                         
        return True              