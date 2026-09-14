class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left,right=0,0
        count={}
        max_length = 0
        for right in range (len(s)):
            ws=right-left+1
            if s[right] in count:
                count[s[right]]+=1
            else:
                count[s[right]]=1
            mf=max(count.values())
            rn=ws-mf
            if rn>k:
                count[s[left]]-=1
                left+=1    
            max_length = max(max_length, right - left + 1)
        return max_length         