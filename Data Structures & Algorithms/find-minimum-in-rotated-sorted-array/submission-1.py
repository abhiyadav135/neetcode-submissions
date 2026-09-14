class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
        nums.sort()
        n=len(nums)
        left,right=0,n-1
        mid=max(nums)
        
