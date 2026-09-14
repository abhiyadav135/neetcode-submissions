class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left,right=0,len(matrix[0])
        mid=left+((right-left)//2)
        for i in range(len(matrix)):
            if target>=matrix[i][0] and target<=matrix[i][-1]:
                f=i 
                break
        else:
            return False        
        while left<=right:
            mid=left+((right-left)//2)
            if matrix[f][mid]==target:  
                return True
            elif target>matrix[f][mid]:
                left=mid+1
            elif target<matrix[f][mid]:
                right=mid-1
        return False            

