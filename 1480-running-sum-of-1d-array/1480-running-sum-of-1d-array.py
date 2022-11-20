class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans2 = []
        
        for i in range(len(nums)):
            total = 0
            for j in range(0,i+1):
                total = nums[j] + total
                
         
            ans2.append(total)
        return ans2