class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left,right=0,k-1
        sums=[]
        while right<len(nums):
            m=max(nums[left:right+1])
            sums.append(m)
            left+=1
            right+=1
        return sums    