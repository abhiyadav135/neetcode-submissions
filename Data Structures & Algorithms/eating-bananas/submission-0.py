class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left,right=1,max(piles)
        mid=left+((right-left)//2)
        res=right
        while left<=right:
            mid=left+((right-left)//2) 
            curr=0
            for i in piles:
                x=math.ceil(i/mid)
                curr+=x
            if curr<=h:
                res=mid
                right=mid-1
                
            else:
                left=mid+1
                   
                    
        return res