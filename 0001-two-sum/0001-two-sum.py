class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
          #hashmaps
        prevMap = {} #val:index
        
        for i , num in enumerate(nums):
            diff = target - num #jo diff ha wo array me dhoond lo
            if diff in prevMap: #jitna chal gia ha utna he dhoonday ga
                return [prevMap[diff] , i]
            prevMap[num] = i
            
                    
        