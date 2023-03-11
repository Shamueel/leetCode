class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #time O(nlogn) 
        '''
        print(nums)
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        '''
        #time O(n)
        pmap = {}
        for i,num in enumerate(nums):
            if nums[i] in pmap:
                return True
            else:
                pmap[num]=i
        #print(pmap)
        
        if 6 in pmap:
            #print("6 in here")
            return False
        
