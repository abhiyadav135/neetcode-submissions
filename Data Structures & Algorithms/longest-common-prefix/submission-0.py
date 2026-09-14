class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        count=0
        min=len(strs[0])
        for i in range(1,len(strs)):
            if len(strs[i])<min:
                min=len(strs[i])

        for j in range(min):
            c=0
            x=strs[0][j]
            for k in range(len(strs)):
                if x==strs[k][j]:
                    c+=1
            if c==len(strs):
                count+=1
            else:
                break    
        return strs[0][0:count]
       