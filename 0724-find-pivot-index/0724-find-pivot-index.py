class Solution:
    
   
    def pivotIndex(self, nums: List[int]) -> int:
        
        '''
        #time limit exceeded with 2 loops
        leftsum = 0
        rightsum = 0
        for i in range(len(nums)):
            if i == 0:
                leftsum = 0
            else:
                leftsum = leftsum + nums[i-1]
           
            for j in range (i+1,len(nums)):
                    rightsum = rightsum + nums[j]
            
            if(rightsum == leftsum):
                return i
            rightsum = 0
        return -1
        '''
        #rightsum is total - left - num[pivot]
        Tsum = sum(nums)
        leftsum = 0
        for i , x in enumerate(nums):
            if leftsum == (Tsum - leftsum - x):
                return i
            leftsum += x
        #incase sol does not exist
        return -1
            
