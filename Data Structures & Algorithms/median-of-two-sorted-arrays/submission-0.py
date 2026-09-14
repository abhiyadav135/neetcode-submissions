class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a,b=nums1,nums2
        total=len(nums1)+len(nums2)
        half=(total+1)//2
        if len(a)>len(b):
            a,b=b,a
        left,right=0,len(a)
        while left<=right:
            i=(left+right)//2
            j=half-i
            aleft=a[i-1] if i>0 else float("-inf")
            aright=a[i] if i<len(a) else float("inf")
            bleft=b[j-1] if j>0 else float("-inf")
            bright=b[j] if j<len(b) else float("inf")

            if aleft<=bright and bleft<=aright:
                if total%2!=0:
                    return float(max(aleft,bleft))
                return (max(aleft,bleft)+min(aright,bright))/2.0
            elif aleft>bright:
                right=i-1
            else:
                left=i+1
        return 0.0            
